from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic import list_detail
from meetup.models import Event

from django.views.generic.simple import redirect_to

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/(.*)', admin.site.root),
    url(r'^about/', redirect_to, {'url': 'http://sunlightfoundation.com/about/'}),
    url(r'^call/', redirect_to, {'url': 'http://sunlightfoundation.com/organizing/'}),
    url(r'^donate/', redirect_to, {'url': 'http://sunlightfoundation.com/donate/'}),
    url(r'^logos/', redirect_to, {'url': 'http://sunlightfoundation.com/press/logos/'}),
    url(r'^news/', redirect_to, {'url': 'http://sunlightfoundation.com/blog/'}),
    url(r'^projects/', redirect_to, {'url': 'http://sunlightfoundation.com/projects/'}),
    url(r'^', redirect_to, {'url': 'http://sunlightfoundation.com/organizing/'}),
)

# urlpatterns = patterns('',
#     url(r'^accounts/', include('registration.backends.default.urls')),
#     url(r'^', include('publicequalsonline.equals.urls')),
#     url(r'^', include('socialregistration.urls')),
#     url(r'^', include('shortcuts.urls')),
# )
# 
# # anthill
# urlpatterns += patterns('',
#     url(r'^call/', include('publicequalsonline.callingtool.urls')),
#     #url(r'^events/', include('anthill.events.urls')),
#     url(r'^people/', include('anthill.people.urls')),
#     url(r'^projects/', include('anthill.projects.urls')),
# )
# 
# # generic views
# urlpatterns += patterns('',
#     url(r'^events/$', list_detail.object_list, {
#         'queryset': Event.objects.filter(account__slug='casino-jack-screenings').exclude(status='past').filter(start_time__isnull=False),
#         'allow_empty': True,
#     }),
# )
# 
# # brainstorm - custom urls so slug isn't needed
# urlpatterns += patterns('brainstorm.views',
#     url(r'^ideas/$', 'idea_list', {'ordering': 'most_popular', 'slug':'ideas'}, name='ideas_popular'),
#     url(r'^ideas/(?P<id>\d+)/$', 'idea_detail', {'slug': 'ideas'}, name='idea_detail'),
#     url(r'^ideas/latest/$', 'idea_list', {'ordering': 'latest', 'slug': 'ideas'}, name='ideas_latest'),
#     url(r'^ideas/new_idea/$', 'new_idea', {'slug': 'ideas'}, name='new_idea'),
#     url(r'^ideas/vote/$', 'vote', name='idea_vote'),
# )
#     
# if (settings.DEBUG):
#     urlpatterns += patterns('',  
#         url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
#     )    