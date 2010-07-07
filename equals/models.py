from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max
from anthill.events.models import Event
from anthill.projects.models import Project, Role, Ask
from anthill.people.signals import message_sent
from brainstorm.models import Idea
from feedinator.models import FeedEntry

CATEGORIES = (
    (1, 'sunlight'),
    (2, 'partner'),
    (3, 'local'),
    (4, 'news'),
)

# features

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

# featured post

class FeaturedPost(Feature):
    image = models.URLField(blank=True, null=True, verify_exists=False)
    source = models.CharField(max_length=255)
    category = models.IntegerField(blank=True, null=True, choices=CATEGORIES)

# pledge count

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

# splash

# class SplashManager(models.Manager):
#     def carousel(self, limit=8):
#         return Splash.objects.filter(is_published=True).order_by('-order')[:limit]
# 
# class Splash(models.Model):
#     objects = SplashManager()
#     name = models.CharField(max_length=128)
#     slug = models.SlugField()
#     url = models.URLField(verify_exists=False)
#     image_url = models.URLField(verify_exists=False)
#     order = models.IntegerField(blank=True, null=True)
#     is_published = models.BooleanField(default=False)
# 
#     class Meta:
#         ordering = ('-order',)
# 
#     def __unicode__(self):
#         return self.name
# 
#     def save(self):
#         if not self.order:
#             max_order = Bumper.objects.aggregate(Max('order'))['order__max'] or 0
#             self.order = max_order + 10
#         super(Bumper, self).save()

# splash button

class SplashButtonManager(models.Manager):
    def published(self, limit=4):
        return SplashButton.objects.filter(is_published=True).order_by('-order')[:limit]

class SplashButton(models.Model):
    objects = SplashButtonManager()
    name = models.CharField(max_length=128)
    slug = models.SlugField()
    url = models.URLField(verify_exists=False)
    image_url = models.URLField(verify_exists=False)
    order = models.IntegerField(blank=True, null=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ('-order',)

    def __unicode__(self):
        return self.name

    def save(self):
        if not self.order:
            max_order = SplashButton.objects.aggregate(Max('order'))['order__max'] or 0
            self.order = max_order + 10
        super(SplashButton, self).save()