""" Module for db request in Actu table"""
from django.core.files.storage import default_storage
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
def delete(request, pk):
    """ deletu photo in db """
    photo = Photo.objects.get(pk=int(pk))
    # delete image
    default_storage.delete(photo.image)
    photo.delete()
