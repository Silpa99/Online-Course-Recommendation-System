from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class CreateProfileForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['username']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','topics_of_interest']

class RatingUpdateForm(forms.ModelForm):
    class Meta:
        model=Rating
        fields=['rating']
