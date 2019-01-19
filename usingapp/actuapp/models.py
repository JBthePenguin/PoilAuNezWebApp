from django.db import models


# Create your models here.
class Actu(models.Model):
    title = models.CharField(db_index=True, max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='actus')
    creating_date = models.DateTimeField(db_index=True, auto_now_add=True)
    change_date = models.DateTimeField(db_index=True, auto_now_add=True)
    author = "Zek"
