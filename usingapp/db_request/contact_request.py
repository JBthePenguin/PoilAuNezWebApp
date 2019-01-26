""" Module for db request in Message table"""
from usingapp.contactapp.models import Message
from managingapp.models import Manager


def save_message(form):
    """ save message """
    managers = Manager.objects.all()
    for manager in managers:
        Message.objects.create(
            contact_name=form.cleaned_data['contact_name'],
            contact_email=form.cleaned_data['contact_email'],
            subject=form.cleaned_data['subject'],
            content=form.cleaned_data['content'],
            status="send",
            recipient=manager,
        )
