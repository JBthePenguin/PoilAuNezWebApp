from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from usingapp.actuapp.models import Actu
from django.contrib.auth.decorators import login_required
from managingapp.actumanagerapp.forms import ActuForm, return_form
from managingapp.db_request import actu_request


@login_required
def actus_manager(request):
    """ return the page with actus for manager,
    display add or modify form for actu with ajax js,
    save and modify Actu with form model"""
    if request.method == 'POST':
        if request.is_ajax():
            action = request.POST.get('action')
            if action == "delete":
                # delete actu
                response = actu_request.delete(request)
                return HttpResponse(response)
            elif action == "display_form":
                # response with add or modify form
                form, hidden_input = return_form(request)
                return HttpResponse(form.as_p() + hidden_input)
        # save and modify actu with form model
        actu_form = ActuForm(request.POST or None, request.FILES or None)
        actu_id = request.POST.get('actu_id')
        try:
            actu_id = int(actu_id)
        except ValueError:
            if (actu_id == "add") and (actu_form.is_valid()):
                # save
                actu_request.save(request, actu_form)
                return redirect('actus_manager')
        else:
            # update actu
            actu_request.update(request, actu_form, actu_id)
            return redirect('actus_manager')
    # GET request
    actus = Actu.objects.all().order_by("change_date").reverse()
    # pagination for header with actus
    if actus.count() == 0:
        actus_pag = False
    else:
        paginator = Paginator(actus, 3)
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
        "form": False,
        "actus": actus_pag,
        "paginate": True,
    }
    return render(request, 'actumanagerapp/actus_manager.html', context)
