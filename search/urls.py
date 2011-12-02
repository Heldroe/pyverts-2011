from django.conf.urls.defaults import *

from search import views


urlpatterns = patterns('',
                       url(r'^(?P<term>\w+)/$',
                           views.search_detail,
                           name='search_detail'),
                       url(r'^$',
                           views.search,
                           name='search'),
                       )
