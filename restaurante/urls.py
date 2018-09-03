from django.contrib import admin
from django.urls import path
from . import views
<<<<<<< HEAD

urlpatterns = [
    path('', views.index, name='index'),
    path('busca/', views.busca_cardapio, name='busca_cardapio'),
    path('add_cardapio/', views.add_cardapio, name="add_cardapio"),
=======
from cardapio import views as views_cardapio

urlpatterns = [
    path('', views.index, name='index'),
    path('busca/', views.busca_restaurante, name='busca_restaurante'),
    path('cardapio/busca/', views_cardapio.busca_cardapio_por_restaurante, name='busca_cardapio_por_restaurante')
>>>>>>> 802543bb969243e22d330984e66ef2d55e18baae
]
