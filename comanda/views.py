from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import login.models
import cardapio.models as cardapio_models
from . import models as comanda_models
from gcm.models import get_device_model
from .forms import pedidoForm, cotaForm

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

@csrf_exempt
def fazer_pedido(request):
    if request.method == 'POST':
        #Add pedido to form
        form = pedidoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            #save form
            pedido = form.save()
            produto = cardapio_models.ProdutoCardapio.objects.get(pk=request.POST.get('produto'))
            user = login.models.Usuario.objects.get(pk=request.POST.get('user'))
            message = 'Deseja dividir ' + produto.nome + ' com ' + user.login + ' por R$ ' + str(produto.preco) + '?'
            #get device
            Device = get_device_model()
            #filter the clients that are in the same table that the order requested
            clientes_mesa = comanda_models.Comanda.objects.filter(mesa=request.POST.get('mesa'))
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
