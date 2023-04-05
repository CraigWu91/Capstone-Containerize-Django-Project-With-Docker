from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.contrib.auth import logout
from django.shortcuts import redirect


# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect('/polls')
    
def show_user(request):
    username = request.user.username
    password = request.user.password
    return render(request, 'authentication/user.html', {
        'username': username,
        'password': password,
    })

def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/polls')
    else:
        form = RegisterUserForm()
    return render(request, 'authentication/registration.html', {'form': form})

