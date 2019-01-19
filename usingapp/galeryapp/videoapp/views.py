from django.shortcuts import render


def videos(request):
    """ return the page with videos """
    context = {
        "galery_page": "active",
        "videos_page": "active"
    }
    return render(request, 'videoapp/videos.html', context)
