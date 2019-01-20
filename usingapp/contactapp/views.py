from django.shortcuts import render
from usingapp.contactapp.forms import ContactForm
from .models import Message


def contact(request):
    """ return the page with contact form"""
    send_msg = False
    form_class = ContactForm
    if request.method == 'POST':
        # message has sent
        form = ContactForm(request.POST)
        if form.is_valid():
            # save message in db
            Message.objects.create(
                contact_name=form.cleaned_data['contact_name'],
                contact_email=form.cleaned_data['contact_email'],
                subject=form.cleaned_data['subject'],
                content=form.cleaned_data['content'],
                status="send",
            )
            send_msg = True
    context = {
        "contact_page": "active",
        'form': form_class,
        'send_msg': send_msg,
    }
    return render(request, 'contactapp/contact.html', context)
