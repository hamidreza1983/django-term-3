from django import forms
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    new_password1 = forms.CharField(max_length=20, widget=forms.PasswordInput)
    new_password2 = forms.CharField(max_length=20, widget=forms.PasswordInput)

class ResetPasswordForm(forms.Form):
    email = forms.EmailField()

class ResetPasswordConfirm(forms.Form):
    new_password1 = forms.CharField(max_length=20, widget=forms.PasswordInput)
    new_password2 = forms.CharField(max_length=20, widget=forms.PasswordInput)
    
