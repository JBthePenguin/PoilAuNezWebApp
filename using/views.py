from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from using.models import Actu

# VIEWS
def index(request):
    """ return the home page """
    context = {"home_page": "active"}
    return render(request, 'using/index.html', context)


def actus(request):
    """ return the page with actus"""
    actus = Actu.objects.all().order_by("change_date").reverse()
    # pagination
    if actus.count() == 0:
        actus_pag = False
    else:
        paginator = Paginator(actus, 4)
        page = request.GET.get('page')
        try:
            actus_pag = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            actus_pag = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page of results.
            actus_pag = paginator.page(paginator.num_pages)
    context = {
        "actus_page": "active",
        "actus": actus_pag,
        "paginate": True,
    }
    return render(request, 'using/actus.html', context)


def galery(request):
    """ return the page with galery"""
    context = {"galery_page": "active"}
    return render(request, 'using/galery.html', context)


def photos(request):
    """ return the page with photos """
    context = {
        "galery_page": "active",
        "photos_page": "active"
    }
    return render(request, 'using/photos.html', context)


def videos(request):
    """ return the page with videos """
    context = {
        "galery_page": "active",
        "videos_page": "active"
    }
    return render(request, 'using/videos.html', context)


def contact(request):
    """ return the page with contact form"""
    context = {"contact_page": "active"}
    return render(request, 'using/contact.html', context)


def mentions(request):
    """ return the page with legal mentions"""
    return render(request, 'using/mentions.html')
