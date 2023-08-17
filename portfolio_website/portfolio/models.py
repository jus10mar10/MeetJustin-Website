from django.db import models
from ckeditor.fields import RichTextField

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = RichTextField()
    image = models.ImageField(upload_to='media/')
    # Add other fields like URL, date, etc.
