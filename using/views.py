from django.shortcuts import render
from using.models import Actu
import datetime


# VIEWS
def index(request):
    """ return the home page """
    context = {"home_page": "active"}
    return render(request, 'using/index.html', context)


def actus(request):
    """ return the page with actus"""
    actus = Actu.objects.all().order_by("change_date").reverse()
    context = {
        "actus_page": "active",
        "actus": actus
    }
    return render(request, 'using/actus.html', context)


def galery(request):
    """ return the page with galery"""
    context = {"galery_page": "active"}
    return render(request, 'using/galery.html', context)


def photos(request):
    """ return the page with photos """
    context = {
        "galery_page": "active",
        "photos_page": "active"
    }
    return render(request, 'using/photos.html', context)


def videos(request):
    """ return the page with videos """
    context = {
        "galery_page": "active",
        "videos_page": "active"
    }
    return render(request, 'using/videos.html', context)


def contact(request):
    """ return the page with contact form"""
    context = {"contact_page": "active"}
    return render(request, 'using/contact.html', context)


def mentions(request):
    """ return the page with legal mentions"""
    return render(request, 'using/mentions.html')
