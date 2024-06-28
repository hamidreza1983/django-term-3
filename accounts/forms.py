from django import forms
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
from django.contrib.auth import get_user_model
User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    captcha = CaptchaField()


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

class EditprofileForm(forms.ModelForm):

    class Meta:
        model  = User
        fields = ['first_name', 'last_name', 'image', 'phone', "id_code"]
    
