from django import forms
from usingapp.actuapp.models import Actu


class ActuForm(forms.ModelForm):

    class Meta:
        model = Actu
        fields = ['image', 'title', 'text']

    def __init__(self, *args, **kwargs):
        super(ActuForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Titre"
        self.fields['text'].label = "Texte"
