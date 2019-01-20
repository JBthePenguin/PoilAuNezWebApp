from django.shortcuts import render


# VIEWS
def index(request):
    """ return the home page """
    context = {"home_page": "active"}
    return render(request, 'usingapp/index.html', context)


def mentions(request):
    """ return the page with legal mentions"""
    return render(request, 'usingapp/mentions.html')
