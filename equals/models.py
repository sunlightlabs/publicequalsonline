from django.contrib.auth.models import User
from feedinator.models import FeedEntry
# from blogdor.models import Post

from django.db import models
# from schedule.models.events import Event
# Create your models here.

CATEGORIES = (
    (1, 'sunlight'),
    (2, 'partner'),
    (3, 'local'),
    (4, 'news'),
)


# def url_to_post(url):
#    from django.core.urlresolvers import resolve
#    view,_,pieces = resolve(url)
#    return Post.objects.get(slug=pieces['slug'], timestamp__year=pieces['year'])
#    popular.register(Post, '^/blog/[0-9]{4}/', url_to_post)

#class Meeting(Event):
#    location = models.CharField(max_length=64, db_index=True)

#
# Features
#

class FeatureManager(models.Manager):
    def published(self):
        return self.model.objects.filter(published=True)

class Feature(models.Model):
    objects = FeatureManager()
    title = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True, verify_exists=False)
    summary = models.TextField(blank=True, null=True)
    published = models.BooleanField(default=False)
    date_published = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        abstract = True
        ordering = ('-date_published',)
    
    def __unicode__(self):
        return self.title

class FeaturedPost(Feature):
    image = models.URLField(blank=True, null=True, verify_exists=False)
    source = models.CharField(max_length=255)
    category = models.IntegerField(blank=True, null=True, choices=CATEGORIES)

class PledgeCountManager(models.Manager):
    def current_count(self):
        try:
            return PledgeCount.objects.get(pk=1)
        except PledgeCount.DoesNotExist:
            p = PledgeCount()
            p.save()
            return p

class PledgeCount(models.Model):
    objects = PledgeCountManager()
    count = models.IntegerField(default=0)
