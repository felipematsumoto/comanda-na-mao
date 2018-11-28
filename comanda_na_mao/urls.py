from django.contrib import admin
from django.urls import include, path
from django.conf.urls import include, url
import cardapio.views
import restaurante.views
import comanda.views
import login.views
import caixa.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cardapio/', include('cardapio.urls')),
    path('restaurante/', include('restaurante.urls')),
    path('comanda/', include('comanda.urls')),
    path('login/', include('login.urls')),
    path('cozinha/', include('cozinha.urls')),
    path('caixa/', include('caixa.urls')),
    path('web_login/',include('login_web.urls'))
    #url(r'', include('gcm.urls'))
]
