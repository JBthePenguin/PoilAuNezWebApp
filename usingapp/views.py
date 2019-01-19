from django.shortcuts import render


# VIEWS
def index(request):
    """ return the home page """
    context = {"home_page": "active"}
    return render(request, 'usingapp/index.html', context)


def contact(request):
    """ return the page with contact form"""
    context = {"contact_page": "active"}
    return render(request, 'usingapp/contact.html', context)


def mentions(request):
    """ return the page with legal mentions"""
    return render(request, 'usingapp/mentions.html')
