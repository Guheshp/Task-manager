from django.forms import ModelForm

from .models import Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput, TextInput


class CreateUserForm(UserCreationForm):
   
   class Meta:
      
      model = User
      fields = ['username','email','password1','password2']

class LoginForm(AuthenticationForm):
   
      username = forms.CharField(widget=TextInput())
      password = forms.CharField(widget=PasswordInput())

class CreateTaskform(forms.ModelForm):

    class Meta:
        model = Task
        fileds = ['title', 'content',]
        exclude = ['user',]


# class UpdateUserForm(forms.ModelForm):

#     password = None

#     class Meta:

#         model = User
#         fileds = ['username', 'email',]
#         exclude = ['password1','password2',]



class UpdateUserProfileForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True