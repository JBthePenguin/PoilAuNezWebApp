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
        actu = Actu.objects.get(pk=actu_id)
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
        default_storage.delete(actu.image)
        actu.delete()
        response = "Actu supprimée"
    return response
