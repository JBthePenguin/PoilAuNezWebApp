from django.db import models
from managingapp.models import Manager


class Message(models.Model):
    contact_name = models.CharField(db_index=True, max_length=255)
    contact_email = models.CharField(db_index=True, max_length=255)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(db_index=True, auto_now_add=True)
    status = models.CharField(db_index=True, max_length=255)
    recipient = models.ForeignKey(
        Manager, default='', on_delete=models.CASCADE)
