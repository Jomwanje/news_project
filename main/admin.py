from django.contrib import admin
from .models import Category,News,Comment

admin.site.register(Category)

class AdminNews(admin.ModelAdmin):
    list_display=('title','category','add_time','youtube_video_id')

admin.site.register(News,AdminNews)

class AdminComment(admin.ModelAdmin):
    list_display=('news','email','comment','status')
admin.site.register(Comment,AdminComment)
