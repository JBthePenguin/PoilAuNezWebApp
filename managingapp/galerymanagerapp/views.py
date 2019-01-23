from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def galery_manager(request):
    """ return the home page """
    return render(request, 'galerymanagerapp/galery_manager.html')
