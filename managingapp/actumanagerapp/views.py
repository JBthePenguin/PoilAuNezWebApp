from django.shortcuts import render, redirect, HttpResponse
from django.core.files.storage import default_storage
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from usingapp.actuapp.models import Actu
from django.contrib.auth.decorators import login_required
from .forms import ActuForm


@login_required
def actus_manager(request):
    """ return the page with actus for manager,
    display add or modify form for actu with ajax js,
    save and modify Actu with form model"""
    form = False
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
    if request.method == 'POST':
        if request.is_ajax():
            # response with add or modify form
            actu_id = request.POST.get('actu_id')
            if actu_id == 'add':
                form = ActuForm()
            else:
                actu = Actu.objects.get(pk=int(actu_id))
                form = ActuForm(instance=actu)
            # add hidden input to keep id for modify form
            hidden_input = "".join([
                "<input type='hidden' ",
                "name='actu_id' value='",
                str(actu_id), "' />"
            ])
            return HttpResponse(form.as_p() + hidden_input)
        # save and modify actu with form model
        actu_form = ActuForm(request.POST or None, request.FILES or None)
        actu_id = request.POST.get('actu_id')
        try:
            actu_id = int(actu_id)
        except ValueError:
            if (actu_id == "add") and (actu_form.is_valid()):
                # save
                # add author
                actu = actu_form.save(commit=False)
                actu.author = request.user
                # save actu in db
                actu.save()
                return redirect('actus_manager')
        else:
            try:
                actu_db = Actu.objects.get(pk=actu_id)
            except KeyError:
                pass
            else:
                # update change of actu
                actu_form.errors
                if actu_form.instance.image != "":
                    # image
                    form_image = request.FILES['image']
                    new_image = default_storage.save(
                        "".join(["actus/", form_image.name]),
                        form_image)
                    default_storage.delete(actu_db.image)
                    actu_db.image = new_image
                    actu_db.change_date = timezone.now()
                    actu_db.save()
                if actu_db.title != actu_form.instance.title:
                    # title
                    actu_db.title = actu_form.instance.title
                    actu_db.change_date = timezone.now()
                    actu_db.save()
                if actu_db.text != actu_form.instance.text:
                    # text
                    actu_db.text = actu_form.instance.text
                    actu_db.change_date = timezone.now()
                    actu_db.save()
                return redirect('actus_manager')
    context = {
        "form": form,
        "actus": actus_pag,
        "paginate": True,
    }
    return render(request, 'actumanagerapp/actus_manager.html', context)


@login_required
def delete_actu(request, pk):
    """ deletu actu in db """
    Actu.objects.get(pk=pk).delete()
    return HttpResponse("Actu supprimée")
