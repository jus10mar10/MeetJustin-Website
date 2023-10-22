from django.shortcuts import render
from .models import Avatar

# Create your views here.

def account(request):
    avatars = Avatar.objects.all()
    return render(request, 'account.html', {'avatars': avatars})