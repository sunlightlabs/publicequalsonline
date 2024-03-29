from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from publicequalsonline.equals.models import FeaturedPost, PledgeCount, Splash, SplashButton
import datetime


from feedinator.models import Feed, FeedEntry, Tag
from feedinator.admin import TagInline

class FeedEntryAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    search_fields = ['title', 'content']
    list_filter = ['feed']
    
admin.site.unregister(FeedEntry)    
admin.site.register(FeedEntry, FeedEntryAdmin)

admin.site.register(PledgeCount)

#
# features
#

class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title','url','published','date_published')
    list_display_links = ('title',)
    list_filter = ('published',)
#    exclude = ('published','date_published')
    actions = ('publish','recall')
    
    def publish(self, request, queryset):
        now = datetime.datetime.now()
        for feature in queryset:
            if not feature.published:
                if not feature.date_published:
                    feature.date_published = now
                feature.published = True
                feature.save()
        self.message_user(request, "%i feature(s) published" % queryset.count())
    publish.short_description = "Publish feature(s)"
    
    def recall(self, request, queryset):
        for feature in queryset:
            if feature.published:
                feature.published = False
                feature.save()
        self.message_user(request, "%i feature(s) recalled" % queryset.count())
    recall.short_description = "Recall feature(s)"

admin.site.register(FeaturedPost, FeatureAdmin)

# splash

class SplashAdmin(admin.ModelAdmin):
    list_display = ('name','active')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Splash, SplashAdmin)

class SplashButtonAdmin(admin.ModelAdmin):
    list_display = ('name','url','image_url','order','is_published')
    list_display_links = ('name',)
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(SplashButton, SplashButtonAdmin)