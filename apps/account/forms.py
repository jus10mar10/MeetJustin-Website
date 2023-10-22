# forms.py
from django import forms
from .models import UserProfile, Avatar

class AvatarSelectForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['selected_avatar']

class AvatarDefaultForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['selected_avatar']
