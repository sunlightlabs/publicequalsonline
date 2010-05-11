from django.contrib import auth
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.contrib.flatpages.views import flatpage
# from blogdor.models import Post
# from blogdor.views import archive
from publicequalsonline.equals.models import FeaturedPost, PledgeCount
from feedinator.models import FeedEntry
from django.db.models import F

from anthill.projects.models import Project
from anthill.events.models import Event
from anthill.people.models import Profile

from django.contrib.gis.shortcuts import render_to_kml


def index(request):
        try:
            featured_blog = FeedEntry.objects.filter(feed__codename='upcoming_events').latest("date_published")
        except FeedEntry.DoesNotExist:
            featured_blog = None


        feature_post = FeaturedPost.objects.filter(published=True).order_by("-date_published")[0:3]
        context = {
        'feature_post': feature_post,
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
 
 
 
    
                             
#def blog_wrapper(request):
#    if 'feed' in request.GET:
#        return HttpResponseRedirect('/blog/feeds/latest')
#    return archive(request)                             


#def register(request):
#    if request.method == 'POST': # If the form has been submitted...
#        form = ContactForm(request.POST) # A form bound to the POST data
#        if form.is_valid(): # All validation rules pass
                # Process the data in form.cleaned_data
                # ...
#            return HttpResponseRedirect('/thanks/') # Redirect after POST
#        else:
#            form = ContactForm() # An unbound form

#        return render_to_response('contact.html', {
#            'form': form,
#        })

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


#def meeting(request):
#    return render_to_response("schedule.html")

#def event_detail(request, id):
#    return render_to_response("event.html")
       

# THESE ARE FOR

def generateEventKml(request):
    locations = Event.objects.all().values('title','description','lat_long')    
    return render_to_kml('events/events.kml',{'locations': locations})
#   return HttpResponse(render_to_string('events/events.kml',{'locations': locations}), mimetype="text/plain")

def generatePeopleKml(request):
    locations = Profile.objects.all().values('user','role','lat_long')
    return render_to_kml('people/people.kml',{'locations': locations})
#   return HttpResponse(render_to_string('people/people.kml',{'locations': locations}), mimetype="text/plain") 

#Projects don't currently have location/geo data associated.
#def generateProjectKml(request):
#    locations = Project.objects.all().values('name','lat_long')
#   return render_to_kml('projects/projects.kml',{'locations': locations})
#    return HttpResponse(render_to_string('projects/projects.kml',{'locations': locations}), mimetype="text/plain") 
       