from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

# handler404 = 'publicequalsonline.equals.views.page_not_found'

urlpatterns = patterns('',
    url(r'^admin/(.*)', admin.site.root),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^', include('publicequalsonline.equals.urls')),
    url(r'^', include('socialregistration.urls')),
)

# anthill
urlpatterns += patterns('',
    url(r'^call/', include('publicequalsonline.callingtool.urls')),
    url(r'^events/', include('anthill.events.urls')),
    url(r'^people/', include('anthill.people.urls')),
    url(r'^projects/', include('anthill.projects.urls')),
)

# brainstorm - custom urls so slug isn't needed
urlpatterns += patterns('brainstorm.views',
    url(r'^ideas/$', 'idea_list', {'ordering': 'most_popular', 'slug':'ideas'}, name='ideas_popular'),
    url(r'^ideas/(?P<id>\d+)/$', 'idea_detail', {'slug': 'ideas'}, name='idea_detail'),
    url(r'^ideas/latest/$', 'idea_list', {'ordering': 'latest', 'slug': 'ideas'}, name='ideas_latest'),
    url(r'^ideas/new_idea/$', 'new_idea', {'slug': 'ideas'}, name='new_idea'),
    url(r'^ideas/vote/$', 'vote', name='idea_vote'),
)
    
if (settings.DEBUG):
    urlpatterns += patterns('',  
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )    