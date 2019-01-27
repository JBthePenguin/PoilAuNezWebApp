""" Module for db request in Actu table"""
import os
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from usingapp.actuapp.models import Actu


@login_required
def save(request, form):
    """ save actu"""
    actu = form.save(commit=False)
    # add author
    actu.author = request.user
    actu.save()
    if 'TRAVIS' not in os.environ:
        # add display url for using with gdrive
        code_img = actu.image.url.split("/")[5]
        actu.display_url_img = "".join(
            ["https://drive.google.com/uc?id=", code_img])
        actu.save()


@login_required
def update(request, form, actu_id):
    """ update actu """
    try:
        actu = Actu.objects.get(pk=actu_id)
    except KeyError:
        pass
    else:
        form.errors
        change_field = False
        if form.instance.image != "":
            form_image = request.FILES['image']
            if 'TRAVIS' not in os.environ:
                from gdstorage.storage import GoogleDriveStorage
                gd_storage = GoogleDriveStorage()
                # storage new and delete old image
                gd_storage.delete(actu.image.name)
                actu.image = gd_storage.save(
                    "".join(["actus/", form_image.name]),
                    form_image)
                actu.save()
                code_img = actu.image.url.split("/")[5]
                actu.display_url_img = "".join(
                    ["https://drive.google.com/uc?id=", code_img])
            else:
                from django.core.files.storage import default_storage
                new_image = default_storage.save(
                    "".join(["actus/", form_image.name]),
                    form_image)
                default_storage.delete(actu.image)
                actu.image = new_image
            change_field = True
        if actu.title != form.instance.title:
            # title
            actu.title = form.instance.title
            change_field = True
        if actu.text != form.instance.text:
            # text
            actu.text = form.instance.text
            change_field = True
        if change_field is True:
            actu.change_date = timezone.now()
            actu.author = request.user
            actu.save()


@login_required
def delete(request):
    """ deletu actu in db """
    actu_id = request.POST.get('object_id')
    try:
        actu = Actu.objects.get(pk=actu_id)
    except KeyError:
        response = "KeyError for actu id"
    else:
        # delete image
        if 'TRAVIS' not in os.environ:
            from gdstorage.storage import GoogleDriveStorage
            gd_storage = GoogleDriveStorage()
            gd_storage.delete(actu.image.name)
        else:
            from django.core.files.storage import default_storage
            default_storage.delete(actu.image)
        actu.delete()
        response = "Actu supprimée"
    return response
