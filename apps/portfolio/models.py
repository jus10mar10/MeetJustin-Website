from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import date


class Post(models.Model):
    class Choices(models.Model):
        TYPE_CHOICES = [
            ('portfolio', 'Portfolio'),
            ('blog', 'Blog'),
        ]
    date = models.DateField(default=None)
    title = models.CharField(max_length=35)
    description = models.TextField(max_length=140)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='thumbnails/')
    type = models.CharField(max_length=20, choices=Choices.TYPE_CHOICES)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=35, null=False)
    email = models.EmailField(null=False)
    message = models.TextField(max_length=140, null=False)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.name
    
class ContentManager(models.Model):
    resume_link = models.CharField(max_length=100, null=False)
    profile_image = models.ImageField(upload_to='profile/')

    class Meta:
        verbose_name_plural = "Content Manager"
