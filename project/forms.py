
from project.models import PostProjects
from django import forms
from django.contrib.auth.models import User,
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class ImageForm(forms.ModelForm):

    class Meta:
        model=PostProjects
        fields=("projects","name")

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']