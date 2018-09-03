from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
<<<<<<< HEAD
from .forms import ProdutoCardapioForm
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from . import models as cardapio_models
=======
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from . import models as restaurante_models
from cardapio.views import busca_cardapio, busca_cardapio_por_restaurante
>>>>>>> 802543bb969243e22d330984e66ef2d55e18baae
import os

@csrf_exempt
def index(request):
<<<<<<< HEAD
    template = loader.get_template("cardapio/Galeria.html")
    return HttpResponse(template.render({}, request))

@csrf_exempt
def add_cardapio(request):
    if request.method == 'POST':
        form = ProdutoCardapioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse(status=201)
        else:
            return JsonResponse(form.errors)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def busca_cardapio(request):
    template = loader.get_template("cardapio/Galeria.html")
    produtos = cardapio_models.ProdutoCardapio.objects.all().filter(nome__icontains=request.POST.get('procura'))
    menu = []
    for p in produtos:
        print(str(os.path.basename(p.foto.name)))
        menu.append({"Nome": str(p.nome), "Arquivo": "cardapio/fotosCardapio/" + str(os.path.basename(p.foto.name))})
    return HttpResponse(template.render({'menu':menu}, request))
=======
    template = loader.get_template("restaurante/Galeria.html")
    return HttpResponse(template.render({}, request))

@csrf_exempt
def busca_restaurante(request):
    template = loader.get_template("restaurante/Galeria.html")
    restaurantes = restaurante_models.Restaurante.objects.all().filter(nome__icontains=request.GET.get('procura'))
    context = []
    for p in restaurantes:
        context.append({"Nome": str(p.nome), "PK": int(p.pk)})
    return HttpResponse(template.render({'context':context}, request))
>>>>>>> 802543bb969243e22d330984e66ef2d55e18baae
