from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^events/$', 'django.views.generic.simple.direct_to_template', {"template": "events.html"}),
    url(r'^pledge/$', 'django.views.generic.simple.direct_to_template', {"template": "pledge.html"}),
    url(r'^actnow/$', 'django.views.generic.simple.direct_to_template', {"template": "actnow.html"}),
    url(r'^groups/$', 'django.views.generic.simple.direct_to_template', {"template": "groups.html"}),
    url(r'^donate/$', 'django.views.generic.simple.direct_to_template', {"template": "local.html"}),   
    url(r'^toolkit/$', 'django.views.generic.simple.direct_to_template', {"template": "toolkit.html"}),
    url(r'^local/$', 'django.views.generic.simple.direct_to_template', {"template": "local.html"}),           
    url(r'^$','publicequalsonline.equals.views.index'),
)


urlpatterns += patterns('publicequalsonline.equals.views',
#    url(r'^$', 'index', name="home"),
)