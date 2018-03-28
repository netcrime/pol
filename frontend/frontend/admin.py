from django.contrib import admin

from models import Feed, Field, FeedField, Post

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('id', 'get_feed', 'get_feed_link', 'created')

    def get_feed(self, obj):
        return obj.feed.uri
    
    def get_feed_link(self, obj):
        return '/feed/%s' % obj.feed.id


class FeedAdmin(admin.ModelAdmin):
    model = Feed
    list_display = ('id', 'uri', 'xpath', 'get_last_update', 'created')

    def get_last_update(self, obj):
        try:
            return Post.objects.filter(feed=obj).latest("created").created
        except:
            return None

class FieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'required')

class FeedFieldAdmin(admin.ModelAdmin):
    model = FeedField
    list_display = ('id', 'get_feed', 'get_field', 'xpath')

    def get_feed(self, obj):
        return obj.feed.uri

    def get_field(self, obj):
        return obj.field.name

admin.site.register(Post, PostAdmin)
admin.site.register(Feed, FeedAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(FeedField, FeedFieldAdmin)
# Register your models here.