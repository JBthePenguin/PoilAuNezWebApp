from django.contrib import admin
from usingapp.galeryapp.videoapp.models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'video', 'creating_date', 'change_date', 'author')
