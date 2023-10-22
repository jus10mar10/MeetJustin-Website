from django.shortcuts import render, redirect
from .models import Avatar
from .forms import AvatarSelectForm
from django.contrib.auth.decorators import login_required

@login_required
def account(request):
    avatars = Avatar.objects.all()
    user_profile = request.user.userprofile
    form = AvatarSelectForm(instance=user_profile)
    
    if request.method == 'POST':
        form = AvatarSelectForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('/account/')  # Replace 'your_redirect_url' with the name of the view or URL where you want to redirect after a successful form submission.
    
    context = {
        'form': form,
        'avatars': avatars,
    }
    return render(request, 'account.html', context)  # Replace 'your_template_name.html' with the appropriate template name.
