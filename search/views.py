#-*- encoding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.template import RequestContext
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from forms import SearchForm
from django.contrib.auth.decorators import login_required

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            #user = User.objects.filter(user=name)
            return HttpResponseRedirect('/search/search_detail/')
    else:
        form = SearchForm()

    return render_to_response('search/search.html',
            {'form': form},
            context_instance=RequestContext(request))

def search_detail(request, term):
    if request.method == 'POST':
        #liste = term
        name = request.POST['name']
        liste = User.objects.filter(username__contains=name)
    return render_to_response('search/search_detail.html',
            {'list': liste},
            context_instance=RequestContext(request))
