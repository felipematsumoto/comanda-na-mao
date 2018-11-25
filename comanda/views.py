from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import login.models
import cardapio.models as cardapio_models
from . import models as comanda_models
from gcm.models import get_device_model
from .forms import pedidoForm, cotaForm
from datetime import datetime
import os

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
    try: #Caso nao esteja em uma mesa
        exists = comanda_models.Comanda.objects.get(user=request.POST.get('usuario'), pago=0)
        return JsonResponse({"Estado":0})
    except comanda_models.Comanda.DoesNotExist:
        user = login.models.Usuario.objects.get(login=request.GET.get('usuario'))
        mesa = comanda_models.Mesa.objects.get(numero=request.GET.get('mesa'), restaurante__pk=request.GET.get('restaurante'))

        comanda_models.Comanda.objects.create(mesa=mesa, user=user, inicio = datetime.now())
        return JsonResponse({"Estado": 1})

@csrf_exempt
def fazer_pedido(request):
    if request.method == 'POST':
        #Add pedido to form
        form = pedidoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            #save form
            pedido = form.save()
            #get Comanda
            comanda = comanda_models.Comanda.objects.get(user=request.POST.get('user'), pago=0)
            #Add Cota
            comanda_models.Cota.objects.create(pedido=pedido,comanda=comanda)

            produto = cardapio_models.ProdutoCardapio.objects.get(pk=request.POST.get('produto'))
            user = login.models.Usuario.objects.get(pk=request.POST.get('user'))
            message = 'Deseja dividir ' + produto.nome + ' com ' + user.login + ' por R$ ' + str(produto.preco) + '?'
            #get device
            Device = get_device_model()
            #filter the clients that are in the same table that the order requested
            clientes_mesa = comanda_models.Comanda.objects.filter(mesa=request.POST.get('mesa'), pago=0)
            #Filter the devices that should receive the alert and send the messages and the order number
            Device.objects.filter(dev_id__in=list(clientes_mesa.values_list('user', flat=True))).exclude(dev_id=request.POST.get('user')).send_message({'message':message, 'pedido':pedido.pk})
            return HttpResponse(status=201)
        else:
            return JsonResponse(form.errors)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def dividir_pedido(request):
    if request.method == 'POST':
        #Add pedido to form
        form = cotaForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            #save form
            form.save()
            return HttpResponse(status=201)
        else:
            return JsonResponse(form.errors)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def lista_pedidos(request):
    import cardapio.models as cardapio_models
    import restaurante.models as restaurante_models
    user = login.models.Usuario.objects.get(login=request.GET.get('usuario'))
    comanda = comanda_models.Comanda.objects.filter(user=user)
    pedidos = comanda_models.Cota.objects.filter(comanda__in=comanda)
    context = {}
    for p in pedidos:
        atual = comanda_models.Pedido.objects.get(pk=p.pedido.pk)
        cota = comanda_models.Cota.objects.filter(pedido=p.pedido.pk).count()
        custo = round((atual.quantidade*atual.produto.preco)/cota,2)
        context.update({atual.pk:{"Custo": custo,"Quantidade":atual.quantidade,
            "Estado":atual.estado,"Nome":atual.produto.nome,"Foto_Produto":"static/cardapio/fotosCardapio/" + str(os.path.basename(atual.produto.foto.name))}})
    return JsonResponse(context)
