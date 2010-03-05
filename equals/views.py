from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.flatpages.views import flatpage
from blogdor.models import Post
from blogdor.views import archive


def index(request):
     return render_to_response("index.html")
    
                             
def blog_wrapper(request):
    if 'feed' in request.GET:
        return HttpResponseRedirect('/blog/feeds/latest')
    return archive(request)                             


def register(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
                # Process the data in form.cleaned_data
                # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
        else:
            form = ContactForm() # An unbound form

        return render_to_response('contact.html', {
            'form': form,
        })

#def meeting(request):
#    return render_to_response("schedule.html")

#def event_detail(request, id):
#    return render_to_response("event.html")
       