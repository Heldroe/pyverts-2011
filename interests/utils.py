from allauth.facebook.models import FacebookAccount
from django.contrib.auth.models import User

from facebook import GraphAPI, GraphAPIError

from time import strptime
import datetime

from models import Interest, UserInterests, InterestCategory

from urllib import urlopen, urlencode, quote_plus
import json
import unicodedata

def strip_accents(s):
       return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

def sync_user_fb_interests(user):
    fb_account = FacebookAccount.objects.get(user=user)
    fb_id = fb_account.social_id
    fb_token = fb_account.token

    graph = GraphAPI(fb_token)
    graph_likes = graph.get_connections(fb_id, "likes")
    likes = graph_likes['data']

    for like in likes:
        like_name = like['name']
        like_category = like['category']
        like_id = like['id']
        try:
            like_date = like['created_time']
            like_creation = strptime(like_date[:-5],"%Y-%m-%dT%H:%M:%S")
            like_datecreation = datetime.date(like_creation.tm_year, like_creation.tm_mon, like_creation.tm_mday)
        except KeyError:
            like_datecreation = datetime.date.today()
        (category, created) = InterestCategory.objects.get_or_create(name=like_category)
        interests = Interest.objects.filter(fb_id=like_id)
        if len(interests) == 0:
            interest = Interest(name=like_name, category=category, fb_id=like_id)
        else:
            interest = interests[0]

        interest.name = like_name
        interest.category = category
        interest.save()

        user_interests = UserInterests.objects.filter(user=user, interest=interest)
        if len(user_interests) == 0:
            user_interest = UserInterests.objects.create(user=user, interest=interest, created=like_datecreation)
        else:
            user_interest = user_interests[0]
        user_interest.created = like_datecreation
        user_interest.save()

def get_score_by_category(user):
    userinterests = UserInterests.objects.filter(user=user)
    scores = {}
    percent = {}
    cat_nbr = 0
    for userinterest in userinterests:
        cat = userinterest.interest.category.name
        if not scores.has_key(cat):
            scores[cat] = 1
        else:
            scores[cat] += 1
    for category in scores.keys():
        percent[category] = int(100*float(scores[category]) / float(len(userinterests)))
    return percent

def get_products_from_interest(interest):
    end_items = []
    query = quote_plus(strip_accents(interest.name))
    json_content = urlopen('https://www.googleapis.com/shopping/search/v1/public/products?key=AIzaSyBBdJ5h1V0q3sAZq339bF389HG0t7u_QV8&country=FR&q='+query+'&alt=json').read()
    json_data = json.loads(json_content)
    try:
        items = json_data['items']
        for item in items:
            try:
                my_item = {}
                my_item['name'] = item['product']['title']
                my_item['description'] = item['product']['description']
                my_item['url'] = item['product']['link']
                my_item['price'] = item['product']['inventories'][0]['price']
                my_item['shipping'] = item['product']['inventories'][0]['shipping']
                my_item['currency'] = item['product']['inventories'][0]['currency']
                my_item['image'] = item['product']['images'][0]['link']
                end_items.append(my_item)
            except KeyError:
                pass
        return end_items
    except KeyError:
        pass
    return end_items
