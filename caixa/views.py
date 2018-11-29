from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import comanda.models
import login.models as x
import cardapio.models


dic = {}

def envia_mesas(request):

    i = 0
    dic = {}
    Id_mesas = []
    comandas = []

    if request.method == 'GET':
        id_restaurante = request.GET.get('ID_restaurante')
        mesas = comanda.models.Mesa.objects.filter(restaurante = id_restaurante)

        for aux in mesas:
            comandas.append( comanda.models.Comanda.objects.filter(mesa = aux))

        for comand in comandas:
            for aux in comand:
                if aux.mesa not in Id_mesas:
                    Id_mesas.append(aux.mesa)

        for aux in Id_mesas:
            dic[i] = {
                    "ID_mesa":  aux.id,
                    "N_mesa":  aux.numero,
                    "ID_restaurante": id_restaurante
                    }
            i += 1

        return render(request, "caixa_mesa.html",{'dic': dic})
    else:
        return HttpResponse()


def envia_comandas_em_aberto(request): #Request

    comandas = []
    dic = {}
    i = 1

    id_restaurante = request.GET.get('ID_restaurante')
    id_mesa = request.GET.get('ID_mesa')
    mesas = comanda.models.Mesa.objects.filter(restaurante = id_restaurante, id = id_mesa)

    dic[0] = {
            "ID_restaurante": id_restaurante
            }

    for aux in mesas:
        comandas.append( comanda.models.Comanda.objects.filter(mesa = aux))

    if request.method == 'GET':
        for comand in comandas:
            for aux in comand:

                if(aux.pago == 0):
                    dic[i] = {
                            "cod_comanda":  aux.id,
                            "Nome_usuario":  x.Usuario.objects.get(id=aux.user_id).login,
                            "ID_restaurante": id_restaurante,
                            "ID_mesa": id_mesa
                            }
                    i += 1
        return render(request, "caixa_Comandas_abertas.html",{'dic': dic})
    else:
        return HttpResponse(status=405)

def calcula_preco(id_pedido):

    i = 0

    cotas = comanda.models.Cota.objects.filter(pedido = id_pedido)
    qtd = comanda.models.Pedido.objects.get(id=str(id_pedido)).quantidade
    preco = cardapio.models.ProdutoCardapio.objects.get(id=comanda.models.Pedido.objects.get(id=str(id_pedido)).produto_id).preco

    for aux in cotas:
        i = 1 + i

    tam = i

    return (preco*qtd)/tam

def mostra_pedido(request):

    comandas = []
    dic = {}
    dic1 = {}
    dic2 = {}
    dic3 = {}
    dic4 = {}
    total = 0
    i = 0

    id_restaurante = request.POST.get('ID_restaurante')
    id_comanda = request.POST.get('ID_comanda')
    id_mesa = request.POST.get('ID_mesa')
    cotas = comanda.models.Cota.objects.filter(comanda = id_comanda)
    mesas = comanda.models.Mesa.objects.filter(restaurante = id_restaurante, id = id_mesa)

    if request.method == 'POST':

        if cotas.exists():
            for aux in cotas:
                id_pedido = aux.pedido
                id_comanda = aux.comanda
                preco = calcula_preco(id_pedido)
                dic1[i] = {
                              "Preco": preco,
                              "Nome_produto": cardapio.models.ProdutoCardapio.objects.get(id=comanda.models.Pedido.objects.get(id=str(id_pedido)).produto_id).nome,
                              "Comentario": comanda.models.Pedido.objects.get(id=str(id_pedido)).coment,
                              "Quantidade": comanda.models.Pedido.objects.get(id=str(id_pedido)).quantidade,
                              "Tamanho": cardapio.models.ProdutoCardapio.objects.get(id=comanda.models.Pedido.objects.get(id=str(id_pedido)).produto_id).tamanhoEmPessoas

                        }
                total = preco + total
                i += 1

            dic[0] = dic1
            i = 0


            for aux in mesas:
                comandas.append( comanda.models.Comanda.objects.filter(mesa = aux))

            for comand in comandas:
                for aux in comand:
                    if(aux.pago == 0):
                        dic2[i] = {
                                   "cod_comanda":  aux.id,
                                   "Nome_usuario":  x.Usuario.objects.get(id=aux.user_id).login,
                                   "ID_restaurante": id_restaurante,
                                   "ID_mesa": id_mesa
                                  }
                        i += 1
            dic[1] = dic2

            dic[2] = {
                      "ID_comanda": id_comanda.id,
                      "ID_restaurante": id_restaurante,
                      "ID_mesa": id_mesa,
                      "total":total
                     }

            return render(request, "detalhes_pedido.html",{'dic': dic})
        else:
            dic[0] = {}
            for aux in mesas:
                comandas.append( comanda.models.Comanda.objects.filter(mesa = aux))

            for comand in comandas:
                for aux in comand:
                    if(aux.pago == 0):
                        dic2[i] = {
                                   "cod_comanda":  aux.id,
                                   "Nome_usuario":  x.Usuario.objects.get(id=aux.user_id).login,
                                   "ID_restaurante": id_restaurante,
                                   "ID_mesa": id_mesa
                                  }
                        i += 1
            dic[1] = dic2

            dic[2] = {
                      #"ID_comanda": id_comanda.id,
                      "ID_restaurante": id_restaurante,
                      "ID_mesa": id_mesa
                     }
            return render(request, "detalhes_pedido.html",{'dic': dic})

    else:
        return HttpResponse(status=405)


def fecha_pedido(request):

        comandas = []
        Id_mesas = []
        dic = {}
        i = 0

        id_mesa = request.POST.get('ID_mesa')
        id_comanda = request.POST.get('ID_comanda')
        id_restaurante = request.POST.get('ID_restaurante')
        print(id_restaurante)
        mesas = comanda.models.Mesa.objects.filter(restaurante = id_restaurante, id = id_mesa)

        for aux in mesas:
            comandas.append( comanda.models.Comanda.objects.filter(mesa = aux))

        if request.method == 'POST':

            t = comanda.models.Comanda.objects.get(id=id_comanda)
            t.pago = 1
            t.save()

            mesas = comanda.models.Mesa.objects.filter(restaurante = id_restaurante)

            for aux in mesas:
                comandas.append( comanda.models.Comanda.objects.filter(mesa = aux))

            for comand in comandas:
                for aux in comand:
                    if aux.mesa not in Id_mesas:
                        Id_mesas.append(aux.mesa)

            for aux in Id_mesas:
                dic[i] = {
                        "ID_mesa":  aux.id,
                        "N_mesa":  aux.numero,
                        "ID_restaurante": id_restaurante
                        }
                i += 1

            return render(request, "caixa_mesa.html",{'dic': dic})
        else:
            return HttpResponse(status=405)
