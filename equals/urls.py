from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^events/$', 'django.views.generic.simple.direct_to_template', {"template": "events.html"}),
    url(r'^$','equalsonline.equals.views.index'),
)


# urlpatterns += patterns('equalsonline.equals.views',
#    url(r'^$', 'index', name="home"),
#    url(r'^(?P<url>.+)(/?)', 'flatpage_wrapper'),
    #)