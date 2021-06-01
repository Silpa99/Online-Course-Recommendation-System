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

class RateForm(ModelForm):
    #RATE_CHOICES = [('like', 'Like'),
                   # ('dislike', 'Dislike'),]
    #rating = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.RadioSelect())
    class Meta:

        model=Rating
        #rating = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.RadioSelect())
        fields=['student_id','course_id','rating']
        '''widgets = {
            'rating': forms.RadioSelect()
        }'''
        #favorite_fruit = forms.CharField(label='What is your favorite fruit?',
                                        # widget=forms.RadioSelect(choices=FRUIT_CHOICES))

