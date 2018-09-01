from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import ProdutoCardapioForm
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
def index(request):
    template = loader.get_template("cardapio/Galeria.html")
    context = {}
    return HttpResponse(template.render(context, request))

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

def busca_cardapio(request):
    return HttpResponse("<h1>Busca Cardapio</h1>")
