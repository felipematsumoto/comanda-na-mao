from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import login.models
import json
from . import models as comanda_models

@csrf_exempt
def index(request):
    return JsonResponse({"Teste":10})

@csrf_exempt
def libera_comanda(request): #Request -> usuario|mesa|restaurante
    user = login.models.Usuario.objects.get(login=request.GET.get('usuario'))
    if user.mesa: #Caso esteja em uma mesa
        #fecha_comanda(user.comanda)
        comanda_models.Comanda.objects.get(mesa=request.GET.get('mesa'), idusuario=user.pk).delete()
        user.mesa = None
        user.comanda = None
        user.save()
        return JsonResponse({"Estado":1})
    else:
        return JsonResponse({"Estado": 0})


@csrf_exempt
def inicia_comanda(request): #Request -> usuario|mesa|restaurante
    user = login.models.Usuario.objects.get(login=request.GET.get('usuario'))
    if not user.mesa: #Caso nao esteja em uma mesa
        mesa = comanda_models.Mesa.objects.get(numero=request.GET.get('mesa'), restaurante__pk=request.GET.get('restaurante'))
        comanda = comanda_models.Comanda(mesa=mesa, idusuario=user.pk)
        comanda.save()
        user.comanda = comanda
        user.mesa = mesa
        user.save()
        return JsonResponse({"Estado":1})
    else:
        return JsonResponse({"Estado": 0})

def lista_pedidos(request):
    import cardapio.models as cardapio_models
    import restaurante.models as restaurante_models
    user = login.models.Usuario.objects.get(login=request.GET.get('usuario'))
    comanda = comanda_models.Comanda.objects.filter(user=user)
    pedidos = comanda_models.Cota.objects.filter(comanda__in=comanda)
    print(pedidos)
    context = {}
    for p in pedidos:
        atual = comanda_models.Pedido.objects.get(pk=p.pedido.pk)
        context.update({atual.pk:{"Custo":atual.custo,"Estado":atual.estado,"Coment":atual.coment,"Foto_Produto":json.dumps(str(atual.produto.foto))}})
    print(context)
    return JsonResponse(context)