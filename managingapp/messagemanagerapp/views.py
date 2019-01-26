import json
from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from usingapp.contactapp.models import Message
from managingapp.db_request import message_request


@login_required
def message_manager(request):
    """ return the page with messages for manager,
    display and delete message with ajax js """
    if request.method == 'POST' and request.is_ajax():
        action = request.POST.get('action')
        if action == "delete":
            # delete message
            response = message_request.delete(request)
            return HttpResponse(response)
        elif action == "display_message":
            # response with message
            response = message_request.return_message(request)
            print(response)
            return HttpResponse(
                json.dumps(response), content_type="application/json")
    # GET
    # select messages for the manager logged
    messages = Message.objects.filter(recipient=request.user)
    # pagination for header with messages
    if messages.count() == 0:
        messages_pag = False
    else:
        paginator = Paginator(messages, 5)
        page = request.GET.get('page')
        try:
            messages_pag = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            messages_pag = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page of results.
            messages_pag = paginator.page(paginator.num_pages)
    context = {
        "messages": messages_pag,
        "paginate": True,
    }
    return render(request, 'messagemanagerapp/message_manager.html', context)
