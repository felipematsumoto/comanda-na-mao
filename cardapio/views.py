from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import ProdutoCardapioForm
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from . import models as cardapio_models
from restaurante import models as restaurante_models
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
    produtos = cardapio_models.ProdutoCardapio.objects.all().filter(nome__icontains=request.GET.get('procura'))
    menu = []
    for p in produtos:
        print(str(os.path.basename(p.foto.name)))
        menu.append({"Nome": str(p.nome), "Arquivo": "cardapio/fotosCardapio/" + str(os.path.basename(p.foto.name))})
    return HttpResponse(template.render({'menu':menu}, request))

@csrf_exempt
def busca_cardapio_por_restaurante(request):
    template = loader.get_template("cardapio/Galeria.html")
    produtos = cardapio_models.ProdutoCardapio.objects.all().filter(restaurante=request.GET.get('restaurante'))
    menu = []
    for p in produtos:
        print(str(os.path.basename(p.foto.name)))
        menu.append({"Nome": str(p.nome), "Arquivo": "cardapio/fotosCardapio/" + str(os.path.basename(p.foto.name))})
    return HttpResponse(template.render({'menu':menu}, request))

@csrf_exempt
def mostrar_cardapio(request):
    #checar o restaurante

    #Pega produtos por filtro
    produtos = 0
    procura = request.GET.get('procura')
    if procura == 'Tudo':
        produtos = cardapio_models.ProdutoCardapio.objects.all().filter(restaurante__nome=request.GET.get('restaurante'))
    else:
        produtos = cardapio_models.ProdutoCardapio.objects.all().filter(tipoProduto__nome=request.GET.get('procura'), restaurante__nome=request.GET.get('restaurante'))
    fimlinha = 0
    menu = []
    for p in produtos:
        menu.append({
                     "Nome": str(p.nome),
                     "Descricao": str(p.descricao),
                     "Tamanho" : int(p.tamanhoEmPessoas),
                     "Preco" : float(p.preco) ,
                     "Tipo": str(p.tipoProduto),
                     "Fimlinha": fimlinha,
                     "Arquivo": "/fotosCardapio/" + str(os.path.basename(p.foto.name))

                     })
        fimlinha = fimlinha + 1
        if fimlinha == 3:
            fimlinha = 0
    tipos = cardapio_models.TipoProduto.objects.all()
    botoes = []
    botoes.append({"Nome": 'Tudo'})
    for t in tipos:
        botoes.append({"Nome": str(t.nome)})

    data = { "menu": menu , "botoes": botoes} #request.GET.get('restaurante')}


    return JsonResponse(data)

@csrf_exempt
def pegar_tipos(request):

    if request.method == 'GET':
        tipos = cardapio_models.TipoProduto.objects.all()
        botoes = []
        for t in tipos:
            botoes.append({"Nome": str(t.nome), "Id": t.id})

        rests = restaurante_models.Restaurante.objects.all().filter(dono__login=request.GET.get('login'))
        restaurantes = []
        for r in rests:
            restaurantes.append({"Nome": str(r.nome), "Id": r.id})



    data = { "tipos": botoes, "restaurantes": restaurantes} #request.GET.get('restaurante')}
    return JsonResponse(data)
