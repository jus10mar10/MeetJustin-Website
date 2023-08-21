from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

class Project(models.Model):
    date = models.DateField(default=timezone.now().date)
    title = models.CharField(max_length=35)
    description = models.TextField(max_length=140)
    content = RichTextField()
    image = models.ImageField(upload_to='thumbnails/')
