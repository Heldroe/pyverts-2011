from django.conf.urls.defaults import *

from interests import views

urlpatterns = patterns('',
                       url(r'^(?P<fb_id>\w+)/$',
                           views.interest_page,
                           name='interest_view'),
                       )
