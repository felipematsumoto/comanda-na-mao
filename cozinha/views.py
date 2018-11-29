
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import comanda.models
import cardapio.models
from .forms import aux_Form

dic = {}

def envia_pedido_para_cozinha(request): #Request -> usuario|mesa|restaurante

    id_restaurante = request.GET.get('ID_restaurante')
    mesas = comanda.models.Mesa.objects.filter(restaurante = id_restaurante)
    pedidos = []
    dic = {}
    i = 1
    dic[0] = {
            "ID_restaurante": id_restaurante
            }
    if request.method == 'GET':
        for aux in mesas:
            comandas = comanda.models.Comanda.objects.filter(mesa = aux)
            for aux1 in comandas:
                cotas = comanda.models.Cota.objects.filter(comanda = aux1.id)
                for aux2 in cotas:
                    pedidos.append( comanda.models.Pedido.objects.filter(id = str(aux2.pedido)))  #Estado igual a 0 o pedido esta em espera, estado igual a 1 o pedido esta em andamenrto e estado igual a 2 pedido esta pronto

        for pedido in pedidos:
            for aux in pedido:
                mesas = comanda.models.Cota.objects.filter(pedido = aux.id)
                for aux1 in mesas :
                    mesa = aux1.comanda.mesa
                dic[i] = {
                        "Nome_produto": str(cardapio.models.ProdutoCardapio.objects.get(id=aux.produto_id).nome),
                        "Comentario": str(aux.coment),
                        "Tamanho": cardapio.models.ProdutoCardapio.objects.get(id=aux.produto_id).tamanhoEmPessoas,
                        "Estado":str(aux.estado),
                        "ID":aux.id,
                        "Quantidade": aux.quantidade,
                        "Mesa": mesa,
                        "ID_restaurante": id_restaurante
                        }
                i += 1
        return render(request, "kanban.html",{'dic': dic})
    else:
        return HttpResponse(status=405)


def muda_estado_pedido(request):
    pedidos = []
    dic = {}
    i = 1

    id_aux = request.POST.get('ID')
    Transicao_aux = request.POST.get('Transicao')
    id_restaurante = request.POST.get('ID_restaurante')

    dic[0] = {
            "ID_restaurante": id_restaurante
            }

    mesas = comanda.models.Mesa.objects.filter(restaurante = id_restaurante)

    for aux in mesas:
        comandas = comanda.models.Comanda.objects.filter(mesa = aux)
        for aux1 in comandas:
            cotas = comanda.models.Cota.objects.filter(comanda = aux1.id)
            for aux2 in cotas:
                pedidos.append( comanda.models.Pedido.objects.filter(id = str(aux2.pedido)))

    if request.method == 'POST':

        t = comanda.models.Pedido.objects.get(id=id_aux)
        t.estado = Transicao_aux
        t.save()
        for pedido in pedidos:
            for aux in pedido:

                dic[i] = {
                        "Nome_produto": str(cardapio.models.ProdutoCardapio.objects.get(id=aux.produto_id).nome),
                        "Comentario": str(aux.coment),
                        "Tamanho": cardapio.models.ProdutoCardapio.objects.get(id=aux.produto_id).tamanhoEmPessoas,
                        "Estado":str(aux.estado),
                        "ID":aux.id,
                        "Quantidade": aux.quantidade,
                        "Mesa": comanda.models.Cota.objects.get(pedido = aux.id).comanda.mesa,  "Mesa": comanda.models.Cota.objects.get(pedido = aux.id).comanda.mesa,
                        "ID_restaurante": id_restaurante
                        }
                i += 1
        return render(request, "kanban.html",{'dic': dic})
    else:
        return HttpResponse(status=405)
