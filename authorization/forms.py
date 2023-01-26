from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=64, label='Name')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid mailing address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Name')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    class Meta:
        model = User
        fields = ('username', 'password',)
