from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('busca/', views.busca_cardapio, name='busca_cardapio'),
    path('add_cardapio/', views.add_cardapio, name="add_cardapio"),
    path('cardapio/', views.mostrar_cardapio, name="mostrar_cardapio"),
    path('tipos/', views.pegar_tipos, name="pegar_tipos"),
]
