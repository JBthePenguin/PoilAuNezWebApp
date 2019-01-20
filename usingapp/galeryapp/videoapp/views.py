from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from usingapp.galeryapp.videoapp.models import Video


def videos(request):
    """ return the page with videos """
    videos = Video.objects.all().order_by("change_date").reverse()
    if videos.count() == 0:
        videos_pag = False
    else:
        paginator = Paginator(videos, 4)
        page = request.GET.get('page')
        try:
            videos_pag = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            videos_pag = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page of results.
            videos_pag = paginator.page(paginator.num_pages)
    context = {
        "galery_page": "active",
        "videos_page": "active",
        "videos": videos_pag,
        "paginate": True,
    }
    return render(request, 'videoapp/videos.html', context)
