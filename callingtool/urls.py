from django.conf.urls.defaults import *

urlpatterns = patterns('callingtool.views',

    url(r'^$', 'legislator_list', name='legislator_list'),

    url(r'^call/(?P<id>\d+)/$', 'call_legislator', name='call_legislator'),

    url(r'^state_senators/(?P<state>[A-Z]{2})/$', 'state_senators', name='state_senators'),

    url(r'^submit_call/(?P<id>\d+)/$', 'submit_call', name='submit_call'),

    url(r'^all_calls/$', 'all_calls', name='all_calls'),
    url(r'^delete_call/(?P<id>\d+)/$', 'delete_call', name='delete_call'),
    
    
    
    
    
    
    
    
    #url(r'^reset/$', 'reset', name='reset'),

)
