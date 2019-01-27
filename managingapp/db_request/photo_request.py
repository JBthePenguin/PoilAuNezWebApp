""" Module for db request in Actu table"""
import os
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from usingapp.galeryapp.photoapp.models import Photo


@login_required
def save(request, form):
    """ save photo"""
    photo = form.save(commit=False)
    # add author
    photo.author = request.user
    photo.save()
    if 'TRAVIS' not in os.environ:
        # add display url for using with gdrive
        code_img = photo.image.url.split("/")[5]
        photo.display_url_img = "".join(
            ["https://drive.google.com/uc?id=", code_img])
        photo.save()


@login_required
def update(request, form, photo_id):
    """ update photo """
    try:
        photo = Photo.objects.get(pk=photo_id)
    except KeyError:
        pass
    else:
        form.errors
        if photo.title != form.instance.title:
            # title
            photo.title = form.instance.title
            photo.change_date = timezone.now()
            photo.author = request.user
            photo.save()


@login_required
def delete(request):
    """ deletu photo in db """
    photo_id = request.POST.get('object_id')
    try:
        photo = Photo.objects.get(pk=photo_id)
    except KeyError:
        response = "KeyError for photo id"
    else:
        if 'TRAVIS' not in os.environ:
            from gdstorage.storage import GoogleDriveStorage
            gd_storage = GoogleDriveStorage()
            # delete image
            gd_storage.delete(photo.image.name)
        else:
            from django.core.files.storage import default_storage
            default_storage.delete(photo.image)
        photo.delete()
        response = "Photo supprimée"
    return response
