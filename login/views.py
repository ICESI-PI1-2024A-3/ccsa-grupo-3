from django.shortcuts import render, redirect
# Decorador
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.


def login(request):
    return render(request, 'registration/login.html')


def home(request):
    return render(request, 'home.html')


def products(request):
    return render(request, 'products.html')


def exit(request):
    logout(request)
    return redirect('login')
