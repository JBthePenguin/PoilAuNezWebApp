from django.contrib import admin
from usingapp.galeryapp.photoapp.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'image', 'creating_date', 'change_date', 'author')
