from django.db import models

from feedinator.models import FeedEntry
from blogdor.models import Post
from schedule.models.events import Event
# Create your models here.


def url_to_post(url):
    from django.core.urlresolvers import resolve
    view,_,pieces = resolve(url)
    return Post.objects.get(slug=pieces['slug'], timestamp__year=pieces['year'])
    popular.register(Post, '^/blog/[0-9]{4}/', url_to_post)


class Meeting(Event):
    location = models.CharField(max_length=64, db_index=True)