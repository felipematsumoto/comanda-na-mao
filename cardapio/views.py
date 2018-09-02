from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import ProdutoCardapioForm
from django.views.decorators.csrf import csrf_exempt

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
