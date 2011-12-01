from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url('', include('allauth.urls')),
    url(r'^profile/',include('profiles.urls')),
    url(r'^$', direct_to_template, {'template': 'home.html',
                                    'extra_context': {'homepage':True}},
                                    name="home"),
    (r'^avatar/', include('avatar.urls')),
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^tutorial/', include('tutorial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

if settings.DEBUG:
    from django.views.static import serve
    _media_url = settings.MEDIA_URL
    if _media_url.startswith('/'):
        _media_url = _media_url[1:]
        urlpatterns += patterns('',
            (r'^%s(?P<path>.*)$' % _media_url,
            serve,
            {'document_root': settings.MEDIA_ROOT}))
    del(_media_url, serve)
