from django.db import models
from managingapp.models import Manager


class Video(models.Model):
    title = models.CharField(db_index=True, max_length=255)
    video = models.FileField(upload_to='videos')
    creating_date = models.DateTimeField(db_index=True, auto_now_add=True)
    change_date = models.DateTimeField(db_index=True, auto_now_add=True)
    author = models.ForeignKey(Manager, default='', on_delete=models.CASCADE)
