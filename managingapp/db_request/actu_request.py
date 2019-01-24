""" Module for db request in Actu table"""
from django.core.files.storage import default_storage
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


@login_required
def update(request, form, actu_id):
    """ update actu """
    try:
        actu_db = Actu.objects.get(pk=actu_id)
    except KeyError:
        pass
    else:
        form.errors
        change_field = False
        if form.instance.image != "":
            # storage new and delete old image
            form_image = request.FILES['image']
            new_image = default_storage.save(
                "".join(["actus/", form_image.name]),
                form_image)
            default_storage.delete(actu_db.image)
            actu_db.image = new_image
            change_field = True
        if actu_db.title != form.instance.title:
            # title
            actu_db.title = form.instance.title
            change_field = True
        if actu_db.text != form.instance.text:
            # text
            actu_db.text = form.instance.text
            change_field = True
        if change_field is True:
            actu_db.change_date = timezone.now()
            actu_db.save()


@login_required
def delete(request, pk):
    """ deletu actu in db """
    actu = Actu.objects.get(pk=int(pk))
    # delete image
    default_storage.delete(actu.image)
    actu.delete()
