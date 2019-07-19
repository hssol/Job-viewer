from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import *
import bcrypt

def logreg(request):
    return render(request, 'logreg/login.html')

def register(request):
    if request.method == "POST":
        regerrors = User.objects.register_validator(request.POST)
        if len(regerrors) > 0:
            for key, value in regerrors.items():
                messages.error(request, value, extra_tags="register")
            return redirect('/')
        else:
            hashed_password = bcrypt.hashpw(request.POST['register_password'].encode(), bcrypt.gensalt())
            newUser = User.objects.create(username=request.POST['register_username'], email=request.POST['register_email'], password=hashed_password)
            request.session['username'] = request.POST['register_username']
            request.session['activeuser'] = newUser.id
            return redirect('/dashboard') #update this when using this app in a different project

def login(request):
    if request.method == "POST":
        logerrors = User.objects.login_validator(request.POST)
        if len(logerrors) > 0:
            for key, value in logerrors.items():
                messages.error(request, value, extra_tags="login")
            return redirect('/')
        else:
            request.session['username'] = request.POST['login_username']
            currentUser = User.objects.filter(username=request.POST['login_username'])
            request.session['activeuser'] = currentUser[0].id
            return redirect('/dashboard') #update this when using this app in a different project

