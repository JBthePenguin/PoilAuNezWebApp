from django import forms
from usingapp.contactapp.models import Message
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
    """ class for the forms for add or update actu """

    captcha = CaptchaField()

    class Meta:
        model = Message
        fields = ['contact_name', 'contact_email', 'subject', 'content']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Votre nom:"
        self.fields['contact_name'].widget.attrs.update({'autofocus': True})
        self.fields['contact_email'].label = "Votre email:"
        self.fields['subject'].label = "Objet du message:"
        self.fields['content'].label = "Votre message:"
