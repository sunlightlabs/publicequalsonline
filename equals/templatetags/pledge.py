from django import template
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from publicequalsonline.equals.models import PledgeCount
 
register = template.Library()

@register.simple_tag
def pledge():
    p_count = PledgeCount.objects.current_count()
    return "%d" % p_count.count
    
    
#    register.simple_tag(pledge)
    

#def show_results(poll):
#    choices = PledgeCount.objects.all()
#    return {'choices': choices}
#    register.inclusion_tag('includes/count.html')(show_results)

