from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import comanda.models
import login.models as x
import cardapio.models


dic = {}

def envia_comandas_com_pedidos_para_caixa(request): #Request
    dic = {}
    i = 0

    id_restaurante = request.GET.get('ID_restaurante')
    comandas = []
    mesas = comanda.models.Mesa.objects.filter(restaurante = id_restaurante)
    for aux in mesas:
        comandas.append( comanda.models.Comanda.objects.filter(mesa = aux))
    print(comandas)
    if request.method == 'GET':
        for comand in comandas:
            for aux in comand:
                if(aux.pago == 0):
                    dic[i] = {
                            "cod_comanda":  aux.id,
                            "Nome_usuario":  x.Usuario.objects.get(id=aux.user_id).login,
                            "ID_restaurante": id_restaurante
                            }
                    i += 1
        return render(request, "caixa.html",{'dic': dic})
    else:
        return HttpResponse(status=405)

def mostra_pedido(request):
    dic = {}
    dic1 = {}
    dic2 = {}
    dic3 = {}
    dic4 = {}
    comandas = []
    i = 0

    id_restaurante = request.POST.get('ID_restaurante')
    id_aux = request.POST.get('ID')
    mesas = comanda.models.Mesa.objects.filter(restaurante = id_restaurante)
    cotas = comanda.models.Cota.objects.filter()
    for aux in mesas:
        comandas.append( comanda.models.Comanda.objects.filter(mesa = aux))

    if request.method == 'POST':

        for aux1 in cotas:

            if(str(aux1.comanda_id) == str(id_aux)):
                pedido = aux1.pedido_id
                comanda_aux = aux1.comanda_id
                dic1[i] = {
                      # "ID_comanda" :  comanda.models.Comanda.objects.get(id=comanda_aux).id,
                      # "Nome_usuario":  x.Usuario.objects.get(id=comanda.models.Comanda.objects.get(id=comanda_aux).user_id).login,
                      "Nome_produto": cardapio.models.ProdutoCardapio.objects.get(id=comanda.models.Pedido.objects.get(id=pedido).produto_id).nome,
                      "Comentario": comanda.models.Pedido.objects.get(id=pedido).coment,
                      "Tamanho": cardapio.models.ProdutoCardapio.objects.get(id=comanda.models.Pedido.objects.get(id=pedido).produto_id).tamanhoEmPessoas,
                      "Custo": comanda.models.Pedido.objects.get(id=pedido).custo,
                      "ID_restaurante": id_restaurante
                        }

                i += 1

        i = 0

        for comand in comandas:
            for aux in comand:
                if(aux.pago == 0):
                    dic2[i] = {
                           "cod_comanda":  aux.id,
                           "Nome_usuario":  x.Usuario.objects.get(id=aux.user_id).login,
                           "ID_restaurante": id_restaurante
                            }
                    i += 1
            dic3[0] = {
                        "Nome_usuario": x.Usuario.objects.get(id=comanda.models.Comanda.objects.get(id=comanda_aux).user_id).login,
                        "ID_restaurante": id_restaurante
                        }
            dic4[0] = {
                        "ID":id_aux,
                        "ID_restaurante": id_restaurante
                      }

        print()
        dic[0] = dic1
        dic[1] = dic2
        dic[2] = dic3
        dic[3] = dic4
        print()
        print("Esse primeiro dicionario guarda todos os pedidos de uma comanda")
        print()
        print(dic1)
        print()
        print("Esse segundo dicionario guarda os pedidos em aberto ")
        print()
        print(dic2)
        print()
        print("Esse terceiro dicionario guarda o id da comanda")
        print()
        print(dic3)

        print()
        print("Esse dicionario é o que sera enviado por jss, ele contem os dic anteriores respectivamente")
        print()
        print(dic)
        print()

        return render(request, "caixa.html",{'dic': dic})
    else:
        return HttpResponse(status=405)


def fecha_pedido(request):

        comandas = []
        dic = {}
        i = 0

        id_aux = request.POST.get('ID')
        id_restaurante = request.POST.get('ID_restaurante')
        print(id_restaurante)
        mesas = comanda.models.Mesa.objects.filter(restaurante = id_restaurante)

        for aux in mesas:
            comandas.append( comanda.models.Comanda.objects.filter(mesa = aux))
        print(comandas)
        if request.method == 'POST':

            t = comanda.models.Comanda.objects.get(id=id_aux)
            t.pago = 1
            t.save()

            for comand in comandas:
                for aux in comand:

                    if(aux.pago == 0):
                        dic[i] = {
                                "cod_comanda":  aux.id,
                                "Nome_usuario":  x.Usuario.objects.get(id=aux.user_id).login
                                }
                        i += 1
            return render(request, "caixa.html",{'dic': dic})
        else:
            return HttpResponse(status=405)
