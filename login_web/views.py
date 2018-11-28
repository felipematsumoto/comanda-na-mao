from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from . import models as user_models
import login.models as Usuario_models
import restaurante.models as restaurante_models

from restaurante import models as restaurante_models

import os

def login(request):

    return render(request, "login_web.html",{})

def retorna_id_restaurante(id_login):
    if  restaurante_models.Restaurante.objects.filter(dono=id_login).exists() :
        obj = restaurante_models.Restaurante.objects.get(dono=id_login)
        return obj.id
    else :
        return -1



@csrf_exempt
def entrar (request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('senha')
        
        if Usuario_models.Usuario.objects.filter(login=login, senha=password).exists():
            obj = Usuario_models.Usuario.objects.get(login=login, senha=password)
            if  obj.tipoUser.nome == 'dono':
                return  render(request, "pos_login.html",{'login': login, 'ID_restaurante': retorna_id_restaurante(obj.id)})# JsonResponse({'login': login, 'tipoUser': obj.tipoUser.nome, 'ID': obj.id})
            else:
                return HttpResponse('Não tem permissão para entrar como dono (Essa conta é do tipo usuário)')
        elif Usuario_models.Usuario.objects.filter(email=login, senha=password).exists():
            obj = Usuario_models.Usuario.objects.get(email=login, senha=password)
            if  obj.tipoUser.nome == 'dono':
                return render(request, "pos_login.html",{'ID_restaurante': retorna_id_restaurante(obj.id)})# JsonResponse({'login': login, 'tipoUser': obj.tipoUser.nome, 'ID': obj.id})
            else:
                return HttpResponse('Não tem permissão para entrar como dono (Essa conta é do tipo usuário)')
        else:
            return HttpResponse('login ou senha invalido')
    return HttpResponse(status=405)

@csrf_exempt
def sair_user(request):
    return HttpResponse(status=201)

@csrf_exempt
def get_item(request):
    if request.method == 'POST':
        pagina = request.POST.get('pagina')

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
