from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from equals.feeds import LabsLatestComments, LabsLatestPosts, LabsLatestForTag, LabsLatestForAuthor

admin.autodiscover()


blog_feeds = {
    'latest': LabsLatestPosts, 'comments': LabsLatestComments,
    'tag': LabsLatestForTag, 'author': LabsLatestForAuthor,
}


urlpatterns = patterns('',
    # blog/blogdor
    url(r'^blog/feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': blog_feeds}, name="blogdor_feeds"),
    url(r'^blog/$', 'equalsonline.equals.views.blog_wrapper'),
    url(r'^blog/', include('blogdor.urls')), 
    url(r'^', include('equalsonline.equals.urls')),    
    
    
#schedule
#    url(r'^schedule/$', 'equalsonline.equals.views.meeting', name='meeting'),
#    url(r'^events/(?P<id>\d+)/$', "equalsonline.equals.views.event_detail", name="event_detail"),   
   
#users
#   url(r'^member/(?P<username>\w+)/$', 'user_view', name='user_view'),
   
#registration
#    (r'^accounts/', include('registration.backends.default.urls')),
#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}, name='index'),    
#    url(r'^', include('equalsonline.equals.urls')),


#    url(r'^(?P<url>.+)(/?)', 'flatpage_wrapper'),
)


    
if (settings.DEBUG):
    urlpatterns += patterns('',  
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
#        url(r'^(?P<filename>.*)\.(?P<extension>css|js)$', 'mediasync.views.static'),
    )    