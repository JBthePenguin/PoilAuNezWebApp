from django.contrib.auth.decorators import login_required
from usingapp.contactapp.models import Message


@login_required
def delete(request):
    """ delete message in db """
    message_id = request.POST.get('object_id')
    try:
        message = Message.objects.get(pk=message_id)
    except KeyError:
        response = "KeyError for message id"
    else:
        message.delete()
        response = "Message supprimé"
    return response


@login_required
def return_message(request):
    """ select the message and return response for ajax js"""
    message_id = request.POST.get('message_id')
    try:
        message = Message.objects.get(pk=message_id)
    except KeyError:
        response = "KeyError for message id"
    else:
        response = {
            "contact_name": message.contact_name,
            "contact_email": message.contact_email,
            "date": message.date.strftime("%d/%m/%Y à %H:%M"),
            "subject": message.subject,
            "content": message.content,
        }
        if message.status == "send":
            message.status = "lu"
            message.save()
    return response
