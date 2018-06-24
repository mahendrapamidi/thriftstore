from storeapp.models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')

def login_user(request):
    if request.method == 'POST':
        username, password = request.POST.get('username'), request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')

def logout_user(request):
    logout(request)
    redirect('index')

def register_user(request):
    if request.method == 'POST':
        details = request.POST
        import ipdb
        ipdb.set_trace()
        user = User.objects.create_user(
            username=details['username'],
            password=details['password'],
            email=details['email'],
        )
        user.save()
        user = authenticate(
            request,
            username=details['username'],
            password=details['password']
        )
        if user:
            login(request, user)
            return redirect('index')
    else:
        return render(request, 'register.html')