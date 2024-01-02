from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
]