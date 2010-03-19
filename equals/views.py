from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.flatpages.views import flatpage
# from blogdor.models import Post
# from blogdor.views import archive
from publicequalsonline.equals.models import FeaturedPost, PledgeCount
from feedinator.models import FeedEntry
from django.db.models import F


def index(request):
        try:
            featured_blog = FeedEntry.objects.filter(feed__codename='upcoming_events').latest("date_published")
        except FeedEntry.DoesNotExist:
            featured_blog = None

        feature_post = FeaturedPost.objects.filter(published=True).order_by("-date_published")[0:3]

        context = {
        'feature_post': feature_post,
         }

        return render_to_response("index.html", context)
    
                             
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

#def meeting(request):
#    return render_to_response("schedule.html")

#def event_detail(request, id):
#    return render_to_response("event.html")
       