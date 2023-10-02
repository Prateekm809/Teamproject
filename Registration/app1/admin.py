from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import *
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.admin import UserAdmin
from .models import VideoCompletion
from .models import UserImage
from .models import UserVideos
from .models import UserData

class UserVideosAdmin(admin.ModelAdmin):
    list_display = ('user', 'video_1', 'video_2', 'video_3', 'video_4', 'video_5', 'video_6', 'video_7', 'video_8', 'video_9', 'video_10')


# Register the UserVideos model and its admin class
admin.site.register(UserVideos, UserVideosAdmin)


class UserAdmin(admin.ModelAdmin):
    add_form = AdminsignupForm
    list_display = ('id', 'username', 'email', 'date_joined')
    list_filter = ('date_joined',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class VideoCompletionAdmin(admin.ModelAdmin):
    list_display = ('user', 'completed')  # Define the fields to display in the admin list view


# Register the VideoCompletion model and its admin class
admin.site.register(VideoCompletion, VideoCompletionAdmin)



@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_image',)
    list_filter = ('user',)


class UserDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'height', 'weight', 'sport_choice')  # Define fields to display in the admin list view

admin.site.register(UserData, UserDataAdmin)
