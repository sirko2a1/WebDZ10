from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from quo.settings import db
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

@login_required
def home(request):
    update_user_list()
    users_collection = db['users']
    users = list(users_collection.find())
    return render(request, 'home.html', {'users': users})

def update_user_list():
    users_collection = db['users']
    users_collection.delete_many({})
    for user in User.objects.all():
        users_collection.insert_one({'username': user.username, 'email': user.email})

@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')
