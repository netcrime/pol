from django.contrib import admin

from models import Feed, Field, FeedField, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'created')

admin.site.register(Post, PostAdmin)
# Register your models here.