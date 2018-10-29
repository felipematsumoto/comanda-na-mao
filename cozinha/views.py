
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

    pedidos = comanda.models.Pedido.objects.filter()   #Estado igual a 0 o pedido esta em espera, estado igual a 1 o pedido esta em andamenrto e estado igual a 2 pedido esta pronto

    if request.method == 'GET':
        dic = {}
        i = 0
        for aux in pedidos:

            dic[i] = {
                        "Nome_produto": str(cardapio.models.ProdutoCardapio.objects.get(id=aux.produto_id).nome),
                        "Comentario": str(aux.coment),
                        "Tamanho": cardapio.models.ProdutoCardapio.objects.get(id=aux.produto_id).tamanhoEmPessoas,
                        "Estado":str(aux.estado),
                        "ID":aux.id
                        }
            i += 1
        return render(request, "kanban.html",{'dic': dic})
    else:
        return HttpResponse(status=405)



def muda_estado_pedido(request):

    id_aux = request.POST.get('ID')
    Transicao_aux = request.POST.get('Transicao')
    pedidos = comanda.models.Pedido.objects.filter()
    dic = {}
    i = 0

    if request.method == 'POST':

        t = comanda.models.Pedido.objects.get(id=id_aux)
        print(Transicao_aux)
        t.estado = Transicao_aux
        t.save()
        for aux in pedidos:

            dic[i] = {
                        "Nome_produto": str(cardapio.models.ProdutoCardapio.objects.get(id=aux.produto_id).nome),
                        "Comentario": str(aux.coment),
                        "Tamanho": cardapio.models.ProdutoCardapio.objects.get(id=aux.produto_id).tamanhoEmPessoas,
                        "Estado":str(aux.estado),
                        "ID":aux.id
                        }
            i += 1
        return render(request, "kanban.html",{'dic': dic})
    else:
        return HttpResponse(status=405)
