from django.http import HttpResponse
from django.shortcuts import render
from .forms import Signupform, Loginform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'gallery.html')


def mylogin(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')
