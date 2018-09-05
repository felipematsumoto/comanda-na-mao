from django.contrib import admin
from django.urls import path
from . import views
from cardapio import views as views_cardapio
from .views import add_restaurante
from .views import restaurante_novo
from .views import lista_restaurantes

urlpatterns = [
    path('', views.index, name='index'),
    path('busca/', views.busca_restaurante, name='busca_restaurante'),
    path('cardapio/busca/', views_cardapio.busca_cardapio_por_restaurante, name='busca_cardapio_por_restaurante'),
    path('add_restaurante/',add_restaurante, name= "add_restaurante"),
    path('novo/',restaurante_novo, name= "restaurante_novo"),
    path('list/',lista_restaurantes, name= "lista")
]
