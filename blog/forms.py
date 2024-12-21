from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Post


# create a user form

class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# login a user form

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# create record form

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'cover', 'body']


# update record form
class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'cover', 'body']