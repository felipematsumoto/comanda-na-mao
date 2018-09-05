from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from . import models as restaurante_models
from .models import Restaurante 
from .forms import restauranteForm
from django.shortcuts import render, redirect

from cardapio.views import busca_cardapio, busca_cardapio_por_restaurante
import os

@csrf_exempt
def index(request):
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

def add_restaurante(request):
    return render(request,'restaurante/add_restaurante.html')

def lista_restaurantes(request):
    restaurante = Restaurante.objects.all()
    return render(request, 'restaurante/Lista_de_restaurante.html', {'restaurante': restaurante})

def restaurante_novo(request):
    form = restauranteForm(request.POST,None)
    if form.is_valid():
        form.save()
        return redirect('add_restaurante')
    return render(request, 'restaurante/restaurante_cadastro.html', {'form':form})