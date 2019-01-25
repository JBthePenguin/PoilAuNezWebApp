""" Module for db request in Actu table"""
from django.core.files.storage import default_storage
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
        # delete image
        default_storage.delete(video.video)
        video.delete()
        response = "Vidéo supprimée"
    return response
