from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from using.actu.models import Actu


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
    return render(request, 'actu/actus.html', context)
