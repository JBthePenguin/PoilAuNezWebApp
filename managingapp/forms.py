from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import UserChangeForm
from .models import Manager
from captcha.fields import CaptchaField


class ManagerCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Manager
        fields = ('username', 'email')


class ManagerChangeForm(UserChangeForm):

    class Meta:
        model = Manager
        fields = ('username', 'email')


class ManagerLoginForm(AuthenticationForm):

    captcha = CaptchaField()
