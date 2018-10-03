
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from . import models as restaurante_models
from .models import Restaurante
from .forms import restauranteForm
from django.shortcuts import render, redirect, get_object_or_404

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

def msg(request):
    return HttpResponse("Restaurante adicionado com sucesso")

def lista_restaurantes(request):

    if request.method == 'GET':
        restaurante = Restaurante.objects.all()
        dic = {}
        i = 0
        for aux in restaurante:
            dic[i] = str(aux.nome)
            i += 1
        return JsonResponse(dic)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def add_restaurante(request):
    if request.method == 'POST':
        form = restauranteForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponse(status=201)
        else:
            return JsonResponse(form.errors)
    else:
        return HttpResponse(status=405)
