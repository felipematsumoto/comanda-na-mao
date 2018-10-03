from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import UsuarioForm
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from . import models as user_models
import os


@csrf_exempt
def registrar_user(request):
    if request.method == 'POST':
        argumento = {
            'login': request.POST.get('login'),
            'email': request.POST.get('email'),
            'senha': request.POST.get('senha'),
        }
        form = UsuarioForm(request.POST, argumento)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['login']
            email = userObj['email']
            if not (user_models.Usuario.objects.filter(login=username).exists()) and not (user_models.Usuario.objects.filter(email=email).exists()):
                form.save()
                user = user_models.Usuario.objects.get(login=username)
                user.tipoUser = user_models.TipoConta.objects.get(nome=request.POST.get('tipoUser'))
                user.save()
                return HttpResponse(status=201)
            else:
                return JsonResponse({'mensagem': 'Login ou email já cadastrado.'})
        else:
            return JsonResponse(form.errors)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def entrar_user(request):
    if request.method == 'GET':
        login = request.GET.get('login')
        password = request.GET.get('senha')
        if (user_models.Usuario.objects.filter(login=login, senha=password).exists()) or (user_models.Usuario.objects.filter(email=login, senha=password).exists()):
            return JsonResponse({'mensagem': 'Login efetuado com sucesso'})
        else:
            return JsonResponse({'mensagem': 'Dados inválidos.'})
    return HttpResponse(status=405)

@csrf_exempt
def sair_user(request):
    return HttpResponse(status=201)
