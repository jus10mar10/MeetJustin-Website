from django.db import models
from ckeditor.fields import RichTextField
from datetime import date

class Post(models.Model):
    class Choices(models.Model):
        TYPE_CHOICES = [
            ('portfolio', 'Portfolio'),
            ('resource', 'Resource'),
        ]
    date = models.DateField(default=date.today)
    title = models.CharField(max_length=35)
    description = models.TextField(max_length=140)
    content = RichTextField()
    image = models.ImageField(upload_to='thumbnails/')
    type = models.CharField(max_length=20, choices=Choices.TYPE_CHOICES)