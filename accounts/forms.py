from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    new_password1 = forms.CharField(max_length=20, widget=forms.PasswordInput)
    new_password2 = forms.CharField(max_length=20, widget=forms.PasswordInput)

class ResetPasswordForm(forms.Form):
    email = forms.EmailField()

class ResetPasswordConfirm(forms.Form):
    new_password1 = forms.CharField(max_length=20, widget=forms.PasswordInput)
    new_password2 = forms.CharField(max_length=20, widget=forms.PasswordInput)

class EditprofileForm(forms.ModelForm):

    class Meta:
        model  = Profile
        fields = ['username', 'first_name', 'last_name', 'image', 'phone', "address"]
    
