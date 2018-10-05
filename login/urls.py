from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.registrar_user, name='registrar_user'),
    path('signin/', views.entrar_user, name="entrar_user"),
    path('signout/', views.sair_user, name="sair_user"),
]
