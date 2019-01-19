from django.shortcuts import render
from usingapp.galeryapp.photoapp.models import Photo
from usingapp.galeryapp.videoapp.models import Video


def galery(request):
    """ return the page with galery"""
    photos = Photo.objects.all().order_by("change_date").reverse()
    if photos.count() == 0:
        photos = False
    videos = Video.objects.all().order_by("change_date").reverse()
    if videos.count() == 0:
        videos = False
    context = {
        "galery_page": "active",
        "photos": photos,
        "videos": videos,
    }
    return render(request, 'galeryapp/galery.html', context)
