from django.shortcuts import render


def galery(request):
    """ return the page with galery"""
    context = {"galery_page": "active"}
    return render(request, 'galeryapp/galery.html', context)
