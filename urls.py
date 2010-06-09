from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
# from equals.feeds import LabsLatestComments, LabsLatestPosts, LabsLatestForTag, LabsLatestForAuthor

admin.autodiscover()

# handler404 = 'publicequalsonline.equals.views.page_not_found'

# blog_feeds = {
#    'latest': LabsLatestPosts, 'comments': LabsLatestComments,
#    'tag': LabsLatestForTag, 'author': LabsLatestForAuthor,
# }

urlpatterns = patterns('',
# blog/blogdor
#    url(r'^blog/feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': blog_feeds}, name="blogdor_feeds"),
#    url(r'^blog/$', 'publicequalsonline.equals.views.blog_wrapper'),
#    url(r'^blog/', include('blogdor.urls')), 
    url(r'^admin/(.*)', admin.site.root),   
    url(r'^', include('publicequalsonline.equals.urls')),        
    url(r'^', include('socialregistration.urls')),
    
    
#schedule
#    url(r'^schedule/$', 'equalsonline.equals.views.meeting', name='meeting'),
#    url(r'^events/(?P<id>\d+)/$', "equalsonline.equals.views.event_detail", name="event_detail"),   
   
#users
#   url(r'^member/(?P<username>\w+)/$', 'user_view', name='user_view'),
   
#registration
    (r'^accounts/', include('registration.backends.default.urls')),
#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}, name='index'),    
#    url(r'^', include('publicequalsonline.equals.urls')),
#    url(r'^(?P<url>.+)(/?)', 'flatpage_wrapper'),

#    url(r'^accounts/', include(registration_consumer.urls)),

# anthill
    url(r'^people/', include('anthill.people.urls')),
    url(r'^projects/', include('anthill.projects.urls')),
    url(r'^events/', include('anthill.events.urls')),
)

# brainstorm - custom urls so slug isn't needed
urlpatterns += patterns('brainstorm.views',
    url(r'^ideas/$', 'idea_list', {'ordering': 'most_popular', 'slug':'ideas'}, name='ideas_popular'),
    url(r'^ideas/latest/$', 'idea_list', {'ordering': 'latest', 'slug': 'ideas'}, name='ideas_latest'),
    url(r'^ideas/(?P<id>\d+)/$', 'idea_detail', {'slug': 'ideas'}, name='idea_detail'),
    url(r'^ideas/new_idea/$', 'new_idea', {'slug': 'ideas'}, name='new_idea'),
    url(r'^ideas/vote/$', 'vote', name='idea_vote'),
)


    
if (settings.DEBUG):
    urlpatterns += patterns('',  
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
#       url(r'^(?P<filename>.*)\.(?P<extension>css|js)$', 'mediasync.views.static'),
    )    