from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, RegisterForm, ChangePasswordForm, ResetPasswordForm, ResetPasswordConfirm, EditprofileForm
from django.contrib.auth import login, logout, authenticate, password_validation

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .models import Profile
from django.views.generic import FormView, CreateView
User = get_user_model()

# def login_user(request):
#     if request.method == 'GET':
#         form = LoginForm()
#         context = {
#             'form': form,
#         }
#         return render(request, 'registrations/login.html', context=context)
#     else:
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = request.POST.get('email')
#             password = request.POST.get('password')
#             user = authenticate(username=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('/')
#             else:
#                 messages.add_message(request, messages.ERROR, 'input data is not valid')
#                 return redirect('accounts:login')
#         else:
#             messages.add_message(request, messages.ERROR, 'input data is not valid')
#             return redirect('accounts:login')

class LoginView(FormView):
    template_name = 'registrations/login.html'
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        user = authenticate(username = email, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'input data is not valid')
        return redirect('accounts:login')
        

    

@login_required
def logout_user(request):
    logout(request)
    return redirect('/')

# def signup_user(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('/')
#         else:
#             messages.add_message(request, messages.ERROR, 'Registration failed')
#             return redirect(request.path_info)
#     else:
#         form = RegisterForm()
#         context = {
#             'form': form,
#             }
#         return render(request, 'registrations/signup.html', context=context)

class SignupView(CreateView):
    template_name = 'registrations/signup.html'
    form_class = RegisterForm
    success_url = "/accounts/login"

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
        
    # def form_invalid(self, form):
    #     messages.add_message(self.request, messages.ERROR, 'input data is not valid')
    #     return redirect('accounts:login')




def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form= ChangePasswordForm(request.POST)
            if form.is_valid():
                old_password = request.POST.get('old_password')
                pass1 = request.POST.get('new_password1')
                pass2 = request.POST.get('new_password2')
                user = request.user
                if user.check_password(old_password):
                    if (pass1 == pass2) and (pass1 and pass2) and pass1 != old_password:
                        try:
                            password_validation.validate_password(pass1)
                            user.set_password(pass1)
                            user.save()
                            login(request, user)
                            messages.add_message(request, messages.SUCCESS, 'your password was changed successfully')
                            return redirect('/')
                        except:
                            messages.add_message(request, messages.ERROR, 'your new password is not valid')
                            return redirect('accounts:change_password')

                    else:
                        messages.add_message(request, messages.ERROR, 'your new passwords are not same')
                        return redirect('accounts:change_password')
                else:
                    messages.add_message(request, messages.ERROR, 'your old password is not valid')
                    return redirect('accounts:change_password')

        else:
            form = ChangePasswordForm()
            context = {
                'form': form,
            }
            return render(request, 'registrations/change_password.html', context=context)

from rest_framework.authtoken.models import Token

def reset_password(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST.get('email'))
            token, create = Token.objects.get_or_create(user=user)
            send_mail(
                'Reset Password',
                f'http://127.0.0.1:8000/accounts/reset_password_confirm/{token.key}/' ,
                from_email='noreply@localhost',
                recipient_list=[user.email],
                fail_silently=True,
            )
            return redirect('accounts:reset_password_done')
        except:
            return redirect('accounts:reset_password')

    else:
        form = ResetPasswordForm()
        context = {
            'form': form,
        }
        return render(request, 'registrations/reset_password.html', context=context)

def reset_password_done(request):
    return render(request, 'registrations/reset_password_done.html')

def reset_password_confirm(request, token):
    if request.method == 'POST':
        user_name = Token.objects.get(key=token).user
        user = User.objects.get(username=user_name)
        pass1 = request.POST.get('new_password1')
        pass2 = request.POST.get('new_password2')
        if (pass1 == pass2) and (pass1 and pass2):
            password_validation.validate_password(pass1)
            user.set_password(pass1)
            user.save()
            return redirect('accounts:reset_password_complete')
    else:
        form = ResetPasswordConfirm()
        context = {
            'form': form,
        }
        return render(request, 'registrations/reset_password_confirm.html', context=context)


def reset_password_complete(request):
    return render(request, 'registrations/reset_password_complete.html')

def edit_profile(request, id):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=id)
        if request.method == "POST":
            form = EditprofileForm(request.POST,request.FILES, instance=user)
            if form.is_valid():
                form.save()
                return redirect ('/')
        else:
            form = EditprofileForm(instance=user)
            context = {
                'form' : form
            }
            return render(request, 'registrations/edit_profile.html', context=context)
    else:
        return redirect('accounts:login')