from django.db import models

# Create your models here.
class Image(models.Model):
    photos = models.ImageField(upload_to = 'myimages')
    date = models.DateTimeField(auto_now_add=True)
