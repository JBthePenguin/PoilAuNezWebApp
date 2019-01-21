from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Manager


class ManagerCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Manager
        fields = ('username', 'email')


class ManagerChangeForm(UserChangeForm):

    class Meta:
        model = Manager
        fields = ('username', 'email')
