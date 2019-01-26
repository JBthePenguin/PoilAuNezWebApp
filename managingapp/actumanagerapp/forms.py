from django import forms
from django.contrib.auth.decorators import login_required
from usingapp.actuapp.models import Actu


class ActuForm(forms.ModelForm):
    """ class for the forms for add or update actu """
    class Meta:
        model = Actu
        fields = ['image', 'title', 'text']

    def __init__(self, *args, **kwargs):
        super(ActuForm, self).__init__(*args, **kwargs)
        self.fields['image'].label = "Ajouter une image"
        self.fields['title'].label = "Titre"
        self.fields['text'].label = "Texte"


@login_required
def return_form(request):
    """ select the add or modify form for actu
    and return response for ajax js"""
    actu_id = request.POST.get('object_id')
    if actu_id == 'add':
        # add form
        form = ActuForm()
    else:
        # update form
        actu = Actu.objects.get(pk=int(actu_id))
        form = ActuForm(instance=actu)
    # add hidden input to keep actu_id
    hidden_input = "".join([
        "<input type='hidden' ",
        "name='actu_id' value='",
        str(actu_id), "' />"
    ])
    return form, hidden_input
