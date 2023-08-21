from django.db import models
from ckeditor.fields import RichTextField
from datetime import date

class Project(models.Model):
    date = models.DateField(default=date.today)
    title = models.CharField(max_length=35)
    description = models.TextField(max_length=140)
    content = RichTextField()
    image = models.ImageField(upload_to='thumbnails/')

class Resource(models.Model):
    date = models.DateField(default=date.today)
    title = models.CharField(max_length=35)
    description = models.TextField(max_length=140)
    content = RichTextField()
    image = models.ImageField(upload_to='thumbnails/')
