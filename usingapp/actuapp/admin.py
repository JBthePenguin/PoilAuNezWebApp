from django.contrib import admin
from usingapp.actuapp.models import Actu


@admin.register(Actu)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'text', 'image', 'creating_date', 'change_date', 'author')
