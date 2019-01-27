import os
from django.db import models
from managingapp.models import Manager
if 'TRAVIS' not in os.environ:
    # if you use the local directory uploads, comment the lines below
    from gdstorage.storage import GoogleDriveStorage
    gd_storage = GoogleDriveStorage()


class Video(models.Model):
    title = models.CharField(db_index=True, max_length=255)
    if 'TRAVIS' in os.environ:
        video = models.ImageField(upload_to='video')
    else:
        # if you use the local directory uploads, comment the lines below
        # and use the same than travis
        video = models.FileField(upload_to='videos', storage=gd_storage)
    display_url_video = models.CharField(max_length=255, default='')
    creating_date = models.DateTimeField(db_index=True, auto_now_add=True)
    change_date = models.DateTimeField(db_index=True, auto_now_add=True)
    author = models.ForeignKey(
        Manager, db_index=True, default='',
        on_delete=models.CASCADE)

# to list image in videos on gdrive
# print(gd_storage.listdir('videos'))
