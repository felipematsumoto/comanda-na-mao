from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import ProdutoCardapioForm
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from . import models as cardapio_models
import os

@csrf_exempt
def index(request):
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