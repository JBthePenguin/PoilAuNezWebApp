from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def videos_manager(request):
    """ return the home page """
    return render(request, 'videomanagerapp/videos_manager.html')
