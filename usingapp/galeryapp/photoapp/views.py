from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from usingapp.galeryapp.photoapp.models import Photo


def photos(request):
    """ return the page with photos """
    photos = Photo.objects.all().order_by("change_date").reverse()
    if photos.count() == 0:
        photos_pag = False
    else:
        paginator = Paginator(photos, 6)
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
        "galery_page": "active",
        "photos_page": "active",
        "photos": photos_pag,
        "paginate": True,
    }
    return render(request, 'photoapp/photos.html', context)
