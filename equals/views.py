from django.contrib import auth
from django.contrib.flatpages.views import flatpage
from django.contrib.gis.shortcuts import render_to_kml
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string

from anthill.projects.models import Project
from anthill.events.models import Event
from anthill.people.models import Profile
from feedinator.models import FeedEntry
from publicequalsonline.equals.models import FeaturedPost, PledgeCount, SplashButton

def index(request):
    try:
        featured_blog = FeedEntry.objects.filter(feed__codename='upcoming_events').latest("date_published")
    except FeedEntry.DoesNotExist:
        featured_blog = None
    feature_post = FeaturedPost.objects.filter(published=True).order_by("-date_published")[0:3]
    context = {
        'feature_post': feature_post,
        'splash_buttons': SplashButton.objects.published(),
    }
    return render_to_response("index.html", context, context_instance=RequestContext(request))

def login(request):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
        
            return HttpResponseRedirect("/account/loggedin/")
        else:
            return HttpResponseRedirect("/account/invalid/")
 
def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/account/loggedout/")

#
# utility views to make life easier
#

def page_not_found(request):
    subject = "[404] publicequalsonline.com%s" % request.path 
    message = "See subject for error"
    #mail_admins(subject, message)
    return defaults.page_not_found(request)

def increment_count(request):
    PledgeCount.objects.all().update(count=F('count') + 1)
    return HttpResponseRedirect("http://local.publicequalsonline.com/page/invite/peo")

def get_count(request):
    pc = PledgeCount.objects.current_count()
    return HttpResponse("updateCount(%d);" % pc.count, content_type="application/json")


def news(request):      
    feature_post = FeaturedPost.objects.filter(published=True).order_by("-date_published")[:20]
    data = { "feature_post": feature_post }
    return render_to_response("news.html", data, context_instance=RequestContext(request))
       

# THESE ARE FOR

def generateEventKml(request):
    locations = Event.objects.all().values('title','description','lat_long')    
#    return render_to_kml('events/events.kml',{'locations': locations})
    return HttpResponse(render_to_string('events/events.kml',{'locations': locations}), mimetype="application/vnd.google-earth.kml+xml")

def generatePeopleKml(request):
    locations = Profile.objects.all().values('user','role','lat_long')
#    return render_to_kml('people/people.kml',{'locations': locations})
    return HttpResponse(render_to_string('people/people.kml',{'locations': locations}), mimetype="application/vnd.google-earth.kml+xml") 

#Projects don't currently have location/geo data associated.
#def generateProjectKml(request):
#    locations = Project.objects.all().values('name','lat_long')
#   return render_to_kml('projects/projects.kml',{'locations': locations})
#    return HttpResponse(render_to_string('projects/projects.kml',{'locations': locations}), mimetype="text/plain") 
       