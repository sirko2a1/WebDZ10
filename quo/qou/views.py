# myapp/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pymongo import MongoClient
from .models import User
from quo.settings import db  

def update_user_list():
    users_collection = db['users']
    users_collection.delete_many({}) 
    for user in User.objects.all():
        users_collection.insert_one({'username': user.username, 'email': user.email})

@login_required
def home(request):
    update_user_list()
    users_collection = db['users']
    users = list(users_collection.find())
    return render(request, 'home.html', {'users': users})
