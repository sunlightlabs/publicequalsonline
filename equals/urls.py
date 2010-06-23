from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^about/$', 'django.views.generic.simple.direct_to_template', {"template": "about.html"}, name="about"),
    url(r'^actnow/$', 'django.views.generic.simple.direct_to_template', {"template": "actnow.html"}),
    url(r'^donate/$', 'django.views.generic.simple.direct_to_template', {"template": "donate.html"}),
    #url(r'^events_old/$', 'django.views.generic.simple.direct_to_template', {"template": "events.html"}),
    #url(r'^groups/$', 'django.views.generic.simple.direct_to_template', {"template": "groups.html"}),
    #url(r'^local/$', 'django.views.generic.simple.direct_to_template', {"template": "local.html"}),
    url(r'^news/$', 'publicequalsonline.equals.views.news', name="news"),
    url(r'^pledge/$', 'django.views.generic.simple.direct_to_template', {"template": "pledge.html"}),
    url(r'^pledge/count/$', 'publicequalsonline.equals.views.get_count'),
    url(r'^pledge/2983gsoidfhd289dh/$', 'publicequalsonline.equals.views.increment_count'),
    url(r'^pledge/thanks/$', 'django.views.generic.simple.direct_to_template', {"template": "pledge_thanks.html"}),
    url(r'^pledge/.*$', 'django.views.generic.simple.direct_to_template', {"template": "pledge.html"}),
    #url(r'^signup/$', 'django.views.generic.simple.direct_to_template', {"template": "account.html"}),
    #url(r'^toolkit/$', 'django.views.generic.simple.direct_to_template', {"template": "toolkit.html"}),  
    
    url(r'^events/events.kml', 'publicequalsonline.equals.views.generateEventKml'),
    url(r'^people/people.kml', 'publicequalsonline.equals.views.generatePeopleKml'),
    #url(r'^projects/projects.kml', 'publicequalsonline.equals.views.generateProjectKml'),
        
    #url(r'^error/$', 'django.views.generic.simple.direct_to_template', {"template": "404.html"}), 

    url(r'^$','publicequalsonline.equals.views.index'),
)