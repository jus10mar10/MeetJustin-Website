from .models import UserProfile

def avatar_context(request):
    avatar_url = None
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            avatar_url = user_profile.selected_avatar.image.url
        except UserProfile.DoesNotExist:
            pass
    return {'avatar_url': avatar_url}
