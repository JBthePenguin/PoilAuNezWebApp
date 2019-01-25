from django import forms
from django.contrib.auth.decorators import login_required
from usingapp.galeryapp.photoapp.models import Photo


class AddPhotoForm(forms.ModelForm):
    """ class for the form for add photo """
    class Meta:
        model = Photo
        fields = ['image', 'title']

    def __init__(self, *args, **kwargs):
        super(AddPhotoForm, self).__init__(*args, **kwargs)
        self.fields['image'].label = "Ajouter une photo"
        self.fields['title'].label = "Titre"


class UpdatePhotoForm(forms.ModelForm):
    """ class for the forms for update photo """
    class Meta:
        model = Photo
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super(UpdatePhotoForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Titre"


@login_required
def return_form(request):
    """ select the add or modify form for photo and return it with ajax js"""
    photo_id = request.POST.get('object_id')
    if photo_id == 'add':
        # add form
        form = AddPhotoForm()
    else:
        # update form
        photo = Photo.objects.get(pk=int(photo_id))
        form = UpdatePhotoForm(instance=photo)
    # add hidden input to keep photo_id
    hidden_input = "".join([
        "<input type='hidden' ",
        "name='photo_id' value='",
        str(photo_id), "' />"
    ])
    return form, hidden_input
