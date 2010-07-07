from django import template
from django.shortcuts import render_to_response
from django.template import Context, Template
from django.template.loader import render_to_string
from feedinator.models import FeedEntry
from publicequalsonline.equals.models import PledgeCount, Splash

register = template.Library()

@register.simple_tag
def active(request, pattern):
    import re
    if re.search(pattern, request.path):
        return 'active'
    return ''

@register.simple_tag
def pledge():
    p_count = PledgeCount.objects.current_count()
    return "%d" % p_count.count

@register.simple_tag
def briefs(codenames, count, offset=6):
    offset = int(offset)
    index = int(count) + offset
    entries = FeedEntry.objects.filter(feed__codename__in=codenames.split(',')).order_by("-date_published")[offset:index]
    return render_to_string("feedinator/briefs.html", {"entries": entries})

@register.simple_tag
def splash():
    s = Splash.objects.current()
    if s is None:
        return ''
    content = """<div id="splash-%s">%s</div>""" % (s.slug, s.content)
    return Template(content).render(Context()) if s else ''