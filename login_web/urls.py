from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('signin/', views.entrar, name="entrar"),
    path('signout/', views.sair_user, name="sair_user"),
    path('getitem/', views.get_item, name="get_item")
]
