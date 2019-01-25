from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from usingapp.galeryapp.videoapp.models import Video
from managingapp.galerymanagerapp.videomanagerapp.forms import return_form
from managingapp.galerymanagerapp.videomanagerapp.forms import AddVideoForm
from managingapp.db_request import video_request


@login_required
def videos_manager(request):
    """ return the page with videos for manager,
    display add or modify form for video with ajax js,
    save and modify Video with form model"""
    if request.method == 'POST':
        if request.is_ajax():
            action = request.POST.get('action')
            if action == "delete":
                # delete actu
                response = video_request.delete(request)
                return HttpResponse(response)
            elif action == "display_form":
                # response with add or modify form
                form, hidden_input = return_form(request)
                return HttpResponse(form.as_p() + hidden_input)
        # save and modify video with form model
        video_form = AddVideoForm(request.POST or None, request.FILES or None)
        video_id = request.POST.get('video_id')
        try:
            video_id = int(video_id)
        except ValueError:
            if (video_id == "add") and (video_form.is_valid()):
                # save
                video_request.save(request, video_form)
                return redirect('videos_manager')
        else:
            # update video
            video_request.update(request, video_form, video_id)
            return redirect('videos_manager')
    # GET request
    videos = Video.objects.all().order_by("change_date").reverse()
    if videos.count() == 0:
        videos_pag = False
    else:
        paginator = Paginator(videos, 2)
        page = request.GET.get('page')
        try:
            videos_pag = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            videos_pag = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page of results.
            videos_pag = paginator.page(paginator.num_pages)
    context = {
        "videos": videos_pag,
        "paginate": True,
    }
    return render(request, 'videomanagerapp/videos_manager.html', context)
