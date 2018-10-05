from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import UsuarioForm
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from . import models as user_models

from restaurante import models as restaurante_models

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
                return JsonResponse({'status': 1})
            else:
                return JsonResponse({'status': 0})
        else:
            return JsonResponse(form.errors)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def entrar_user(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('senha')
        if user_models.Usuario.objects.filter(login=login, senha=password).exists():
            obj = user_models.Usuario.objects.get(login=login, senha=password)
            return JsonResponse({'login': login, 'tipoUser': obj.tipoUser.nome, 'ID': obj.id})
        elif user_models.Usuario.objects.filter(email=login, senha=password).exists():
            obj = user_models.Usuario.objects.get(email=login, senha=password)
            return JsonResponse({'login': obj.login, 'tipoUser': obj.tipoUser.nome, 'ID': obj.id})
        else:
            return JsonResponse({'login': "null"})
    return HttpResponse(status=405)

@csrf_exempt
def sair_user(request):
    return HttpResponse(status=201)

@csrf_exempt
def get_item(request):
    if request.method == 'POST':
        obj_tipo = request.POST.get('tipo')
        obj_id = request.POST.get('id')
        context = {}
        if obj_tipo == 'User':
            obj = user_models.Usuario.objects.get(id=obj_id)
            context = {"Login": obj.login, "Email": obj.email}
        elif obj_tipo == 'Restaurante':
            obj = restaurante_models.Restaurante.objects.get(id=obj_id)
            context = {"Nome": obj.nome, "Cnpj": obj.cnpj, "Dono": obj.nomeDono, "Tel": obj.telefone, "End": obj.endereco, "Email": obj.email}
        elif obj_tipo == 'Mesa':
            obj = user_models.Usuario.objects.get(id=obj_id)
        return JsonResponse(context)
