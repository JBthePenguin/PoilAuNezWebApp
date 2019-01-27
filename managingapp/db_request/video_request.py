""" Module for db request in Actu table"""
import os
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from usingapp.galeryapp.videoapp.models import Video


@login_required
def save(request, form):
    """ save video"""
    video = form.save(commit=False)
    # add author
    video.author = request.user
    video.save()
    if 'TRAVIS' not in os.environ:
        # add display url for using with gdrive
        code_video = video.video.url.split("/")[5]
        video.display_url_video = "".join(
            ["https://drive.google.com/uc?id=", code_video])
        video.save()


@login_required
def update(request, form, video_id):
    """ update video """
    try:
        video = Video.objects.get(pk=video_id)
    except KeyError:
        pass
    else:
        form.errors
        if video.title != form.instance.title:
            # title
            video.title = form.instance.title
            video.change_date = timezone.now()
            video.author = request.user
            video.save()


@login_required
def delete(request):
    """ deletu video in db """
    video_id = request.POST.get('object_id')
    try:
        video = Video.objects.get(pk=video_id)
    except KeyError:
        response = "KeyError for video id"
    else:
        if 'TRAVIS' not in os.environ:
            from gdstorage.storage import GoogleDriveStorage
            gd_storage = GoogleDriveStorage()
            # delete video
            gd_storage.delete(video.video.name)
        else:
            from django.core.files.storage import default_storage
            default_storage.delete(video.video)
        video.delete()
        response = "Vidéo supprimée"
    return response
