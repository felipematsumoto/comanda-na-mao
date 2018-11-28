from django.urls import path
from . import views

urlpatterns = [
    path('cozinha/', views.envia_pedido_para_cozinha, name='envia'),
    path('estado/',views.muda_estado_pedido, name='muda'),
    
]
