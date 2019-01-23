from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def message_manager(request):
    """ return the home page """
    return render(request, 'messagemanagerapp/message_manager.html')
