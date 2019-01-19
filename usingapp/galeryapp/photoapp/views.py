from django.shortcuts import render


def photos(request):
    """ return the page with photos """
    context = {
        "galery_page": "active",
        "photos_page": "active"
    }
    return render(request, 'photoapp/photos.html', context)
