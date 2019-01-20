from django import forms


# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    contact_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Votre nom:"
        self.fields['contact_email'].label = "Votre email:"
        self.fields['subject'].label = "Objet du message:"
        self.fields['content'].label = "Votre message:"
