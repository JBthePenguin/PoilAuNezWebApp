from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from usingapp.galeryapp.photoapp.models import Photo
from managingapp.galerymanagerapp.photomanagerapp.forms import return_form
from managingapp.galerymanagerapp.photomanagerapp.forms import AddPhotoForm
from managingapp.db_request import photo_request


@login_required
def photos_manager(request):
    """ return the page with photos for manager,
    display add or modify form for photo with ajax js,
    save and modify Photo with form model"""
    if request.method == 'POST':
        if request.is_ajax():
            action = request.POST.get('action')
            if action == "delete":
                # delete actu
                response = photo_request.delete(request)
                return HttpResponse(response)
            elif action == "display_form":
                # response with add or modify form
                form, hidden_input = return_form(request)
                return HttpResponse(form.as_p() + hidden_input)
        # save and modify photo with form model
        photo_form = AddPhotoForm(request.POST or None, request.FILES or None)
        photo_id = request.POST.get('photo_id')
        try:
            photo_id = int(photo_id)
        except ValueError:
            if (photo_id == "add") and (photo_form.is_valid()):
                # save
                photo_request.save(request, photo_form)
                return redirect('photos_manager')
        else:
            # update photo
            photo_request.update(request, photo_form, photo_id)
            return redirect('photos_manager')
    # GET request
    photos = Photo.objects.all().order_by("change_date").reverse()
    if photos.count() == 0:
        photos_pag = False
    else:
        paginator = Paginator(photos, 4)
        page = request.GET.get('page')
        try:
            photos_pag = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            photos_pag = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page of results.
            photos_pag = paginator.page(paginator.num_pages)
    context = {
        "photos": photos_pag,
        "paginate": True,
    }
    return render(request, 'photomanagerapp/photos_manager.html', context)
