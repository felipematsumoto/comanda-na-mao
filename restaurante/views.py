
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
    if request.method == 'POST':
        filtro = request.POST.get('procura')
        if filtro == '':
            restaurantes = restaurante_models.Restaurante.objects.all()
        elif request.POST.__contains__('pornome'):
            restaurantes = restaurante_models.Restaurante.objects.all().filter(dono__login=filtro)
        else:
            restaurantes = restaurante_models.Restaurante.objects.all().filter(nome__icontains=filtro)
        context = []
        for p in restaurantes:
            context.append({"Nome": str(p.nome),"Id": str(p.id), "Dono": str(p.nomeDono), "End": str(p.endereco), "Tel": str(p.telefone), "Foto": str(os.path.basename(p.foto.name))})
        return JsonResponse({"lista": context})

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

@csrf_exempt
def leitura_restaurante(request):
    p = restaurante_models.Restaurante.objects.get(pk=request.GET.get("id"))
    context = {"Nome": str(p.nome), "PK": int(p.pk), "CNPJ": str(p.cnpj), "nomeDono":str(p.nomeDono), "telefone":str(p.telefone), "endereco":str(p.endereco), "email":str(p.email)}
    return JsonResponse(context)
