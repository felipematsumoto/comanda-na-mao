from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import login.models
from . import models as comanda_models

@csrf_exempt
def index(request):
    return JsonResponse({"Teste":10})

@csrf_exempt
def libera_comanda(request):
    #Pegar a sessao do usuario
    user = login.models.Usuario.objects.get(login=request.GET.get('usuario'))
    print(user.mesa)
    if(user.mesa != -1):
        #Realizar pagamento
        comanda = comanda_models.Comanda.objects.get(mesa=user.mesa)
        mesa = comanda_models.Mesa.objects.get(numero=user.mesa, restaurante__pk=request.GET.get('restaurante'))
        comanda.delete()
        mesa.delete()
        user.mesa = -1
        user.comanda = -1
        user.save()
        print("<:)")
    else:
        print(">:(")
    return JsonResponse({"Teste":20})

@csrf_exempt
def inicia_comanda(request):
    # Pegar a sessao do usuario
    user = login.models.Usuario.objects.get(login=request.GET.get('usuario'))
    print(user.mesa)
    if(user.mesa == -1): #Precisa iniciar uma comanda para este usuario nesta mesa
        user.mesa = request.GET.get("mesa")
        mesa = comanda_models.Mesa.objects.get(numero=user.mesa, restaurante__pk=request.GET.get('restaurante'))
        comanda = comanda_models.Comanda(mesa=mesa)
        comanda.save()
        user.comanda = comanda
        user.save()
        print("<:)")
    else:
        print(">:(")
    return JsonResponse({"Teste": 30})