from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='avatars/')
    # show image
    def image_tag(self):
        from django.utils.html import escape
        return u'<img src="%s" />' % escape('avatars/'+self.image.name)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    if Avatar.objects.filter(name='default').exists():
        selected_avatar = models.ForeignKey(Avatar, null=True, blank=True, on_delete=models.SET_NULL, default=Avatar.objects.get(name='default').id)
    else:
        selected_avatar = models.ForeignKey(Avatar, null=True, blank=True, on_delete=models.SET_NULL)
