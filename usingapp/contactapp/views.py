from django.shortcuts import render
from usingapp.contactapp.forms import ContactForm
from usingapp.db_request import contact_request


def contact(request):
    """ return the page with contact form"""
    send_msg = False
    form = ContactForm
    if request.method == 'POST':
        # message has sent
        form = ContactForm(request.POST)
        if form.is_valid():
            # save message in db
            contact_request.save_message(form)
            send_msg = True
            form = ContactForm
    # GET request
    context = {
        "contact_page": "active",
        'form': form,
        'send_msg': send_msg,
    }
    return render(request, 'contactapp/contact.html', context)
