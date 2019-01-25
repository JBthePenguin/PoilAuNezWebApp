from django import forms
from django.contrib.auth.decorators import login_required
from usingapp.galeryapp.videoapp.models import Video


class AddVideoForm(forms.ModelForm):
    """ class for the form for add video """
    class Meta:
        model = Video
        fields = ['video', 'title']

    def __init__(self, *args, **kwargs):
        super(AddVideoForm, self).__init__(*args, **kwargs)
        self.fields['video'].label = "Ajouter une vidéo"
        self.fields['title'].label = "Titre"


class UpdateVideoForm(forms.ModelForm):
    """ class for the forms for update video """
    class Meta:
        model = Video
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super(UpdateVideoForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Titre"


@login_required
def return_form(request):
    """ select the add or modify form for video and return it with ajax js"""
    video_id = request.POST.get('object_id')
    if video_id == 'add':
        # add form
        form = AddVideoForm()
    else:
        # update form
        video = Video.objects.get(pk=int(video_id))
        form = UpdateVideoForm(instance=video)
    # add hidden input to keep video_id
    hidden_input = "".join([
        "<input type='hidden' ",
        "name='video_id' value='",
        str(video_id), "' />"
    ])
    return form, hidden_input
