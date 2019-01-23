from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def photos_manager(request):
    """ return the home page """
    return render(request, 'photomanagerapp/photos_manager.html')
