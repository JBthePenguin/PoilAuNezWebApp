from django.contrib import admin
from usingapp.contactapp.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    search_fields = ('contact_name',)
    list_display = (
        'contact_name',
        'contact_email',
        'subject',
        'content',
        'date',
        'status',
        'recipient',
    )
