from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import ManagerCreationForm, ManagerChangeForm
from .models import Manager


class ManagerAdmin(UserAdmin):
    add_form = ManagerCreationForm
    form = ManagerChangeForm
    model = Manager
    list_display = [
        'username',
        'is_superuser',
        'is_active',
    ]


admin.site.register(Manager, ManagerAdmin)
