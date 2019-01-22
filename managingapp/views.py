from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from managingapp.forms import ManagerLoginForm


# VIEWS
class ManagerLoginView(LoginView):

    form_class = ManagerLoginForm

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(*args, **kwargs)


def index_member(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')


@login_required
def dashboard(request):
    """ return the home page """
    return render(request, 'managingapp/dashboard.html')


@login_required
def logout_manager(request):
    logout(request)
    return redirect('login')


@login_required
def actus_manager(request):
    """ return the home page """
    return render(request, 'managingapp/actus_manager.html')


@login_required
def galery_manager(request):
    """ return the home page """
    return render(request, 'managingapp/galery_manager.html')


@login_required
def photos_manager(request):
    """ return the home page """
    return render(request, 'managingapp/photos_manager.html')


@login_required
def videos_manager(request):
    """ return the home page """
    return render(request, 'managingapp/videos_manager.html')


@login_required
def message_manager(request):
    """ return the home page """
    return render(request, 'managingapp/message_manager.html')
