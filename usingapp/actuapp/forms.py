from django import forms

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