from django.contrib import admin
from django.urls import include, path
import cardapio.views
import restaurante.views
import comanda.views
import login.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cardapio/', include('cardapio.urls')),
    path('restaurante/', include('restaurante.urls')),
    path('comanda/', include('comanda.urls')),
    path('login/', include('login.urls')),
    path('cozinha/', include('cozinha.urls'))

]
