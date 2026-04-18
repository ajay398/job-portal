from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username=username, password=password)
        messages.success(request, "User created successfully")
        return redirect('login')

    return render(request, 'users/register.html')


def home(request):
    return render(request, 'users/home.html')


def login_view(request):
    return render(request, 'users/login.html')