# Create your views here.

from models import Interest
from django.shortcuts import render_to_response
from django.template import RequestContext

from facebook import GraphAPI, GraphAPIError

from utils import get_products_from_interest

def interest_page(request, fb_id):
    try:
        interest = Interest.objects.get(fb_id=fb_id)
        graph = GraphAPI()
        graph_data = graph.get_connections(fb_id, '/')
        name = graph_data['name']
        items = get_products_from_interest(interest)
        return render_to_response('interests/view.html',
                                  {'fb_id': fb_id,
                                   'fb_name': name,
                                   'items': items},
                                  context_instance=RequestContext(request))
    except Interest.DoesNotExist:
        return render_to_response('interests/view_404.html',
                                  {},
                                  context_instance=RequestContext(request))
        
        
