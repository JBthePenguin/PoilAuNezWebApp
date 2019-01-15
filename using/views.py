from django.shortcuts import render


# VIEWS
def index(request):
    """ return the home page """
    return render(request, 'using/index.html')


def actus(request):
    """ return the page with actus"""
    return render(request, 'using/actus.html')


def galery(request):
    """ return the page with galery"""
    return render(request, 'using/galery.html')


def photos(request):
    """ return the page with photos """
    return render(request, 'using/photos.html')


def videos(request):
    """ return the page with videos """
    return render(request, 'using/videos.html')


def contact(request):
    """ return the page with contact form"""
    return render(request, 'using/contact.html')


def mentions(request):
    """ return the page with legal mentions"""
    return render(request, 'using/mentions.html')
