from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^events/$', 'django.views.generic.simple.direct_to_template', {"template": "events.html"}),
    url(r'^$','publicequalsonline.equals.views.index'),
)


# urlpatterns += patterns('publicequalsonline.equals.views',
#    url(r'^$', 'index', name="home"),
#    url(r'^(?P<url>.+)(/?)', 'flatpage_wrapper'),
    #)