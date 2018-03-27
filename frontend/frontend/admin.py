from django.contrib import admin

from models import Feed, Field, FeedField, Post

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('id', 'get_feed', 'created')

    def get_feed(self, obj):
        return obj.feed.uri


class FeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'uri', 'xpath', 'created')

class FieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'required')

class FeedFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'feed', 'field', 'xpath')

admin.site.register(Post, PostAdmin)
admin.site.register(Feed, FeedAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(FeedField, FeedFieldAdmin)
# Register your models here.