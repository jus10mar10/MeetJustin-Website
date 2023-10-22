from django.contrib import admin
from .models import Avatar
from django.utils.safestring import mark_safe
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'selected_avatar_display')
    fields = ['user', 'selected_avatar']

    def selected_avatar_display(self, obj):
        if obj.selected_avatar:
            return mark_safe('<img src="{}" width="50" height="50" style="border-radius: 50%;" />'.format(obj.selected_avatar.image.url))
        return "No Avatar Selected"
    selected_avatar_display.short_description = 'Selected Avatar'

admin.site.register(UserProfile, UserProfileAdmin)

class PostAvatar(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    fields = ['name','image', 'image_tag']
    readonly_fields = ['image_tag']

    def image_tag(self, obj):
        return mark_safe('<img src="{}" width="150" height="150" style="border-radius: 50%;" />'.format(obj.image.url))

    image_tag.short_description = 'Image Preview'


admin.site.register(Avatar, PostAvatar)
