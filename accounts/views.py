from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_user(request):
    if request.method == 'GET':
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'registrations/login.html', context=context)
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, 'input data is not valid')
            return redirect('accounts:login')

    

@login_required
def logout_user(request):
    logout(request)
    return redirect('/')

def signup_user(request):
    pass

def change_password(request):
    pass

def reset_password(request):
    pass

def reset_password_done(request):
    pass

def reset_password_confirm(request):
    pass

def reset_password_complete(request):
    pass

def edit_profile(request):
    pass