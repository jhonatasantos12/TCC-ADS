from math import prod
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from flask import request
from product import models as ProductModel
from estoque import models as EstoqueModel
from customer import models as CustomerModel
from pedidos import models as PedidosModel
from datetime import datetime
# Create your views here.
def Listadepedidos(request):
    return render(request,'pedidos/ListPedidos.html',
    context={
        "Pedidos": PedidosModel.Pedido.objects.all(),
    }) 
def pedidos(request):
    if request.method !='POST':
        return render(request,'pedidos/StartPedido.html',
        context={
            "Customers": CustomerModel.Customer.objects.all(),
            "Estoque": EstoqueModel.Estoque.objects.all(),
        })
    cliente = request.POST.get('cliente')
    Estoque = EstoqueModel.Estoque.objects.all()
    ProdPedido= {}
    ProdPedido['Produtos'] ={}
    for x in Estoque:
        try:
            produto = request.POST.get(str(x.produto.id))
        except:
            produto = None
        if produto != None:
            limiteEstq = EstoqueModel.Estoque.objects.get(produto = x.produto.id)
            if produto > limiteEstq.Quantidade:
                return HttpResponse('Quantidade informada Indisponivel')
            ProdPedido['Produtos'][str(x.produto.id)] = {}
            ProdPedido['Produtos'][str(x.produto.id)]['Id'] = str(x.produto.id)
            ProdPedido['Produtos'][str(x.produto.id)]['NameProduct'] = str(x.produto.nome)
            ProdPedido['Produtos'][str(x.produto.id)]['Quantidade'] = produto
    if  ProdPedido['Produtos']:
        ProdPedido['Cliente'] =  cliente
        ProdPedido['Categoria'] = True
        ProdPedido['Status'] = "Em Separação"
    else:
        print("Num tem produto bixo")
    Pcliente = CustomerModel.Customer.objects.get(id = ProdPedido['Cliente'])
    pedido = PedidosModel.Pedido.objects.create(Categoria = ProdPedido['Categoria'], Cliente = Pcliente, Status= ProdPedido['Status'])
    pedido.save()
    for x in ProdPedido['Produtos']:
        produto = ProductModel.Product.objects.get(id= x)
        ProdutoPedido = PedidosModel.ProdutoPedido.objects.create(pedido = pedido, produto=produto,quantidade=ProdPedido['Produtos'][str(x)]['Quantidade'])
        ProdutoPedido.save()
        Estoque = EstoqueModel.Estoque.objects.get(produto = produto)
        Estoque.quantidade -= int(ProdPedido['Produtos'][str(x)]['Quantidade']) 
        Estoque.save()
    #PedidosModel.ProdutoPedido
    return render (request,'pedidos/StartPedido.html')



@csrf_exempt
def entrada(request):
    if request.method !='POST':
        return render (request,'pedidos/EntradaEstoque.html',
        context={
            "produtos": ProductModel.Product.objects.all()
        })
    quantidade = request.POST.get('qtd')
    produtoR = request.POST.get('product')
    try:
        tem = EstoqueModel.Estoque.objects.get(produto=produtoR)
    except:
        tem = None
    if tem == None:
        produtoC = ProductModel.Product.objects.get(id = produtoR)
        estoque = EstoqueModel.Estoque.objects.create(produto = produtoC, quantidade = quantidade)
        estoque.save()
    else:
        tem.quantidade  += int(quantidade)
        tem.save()
    print(tem)
    return HttpResponse(produtoR,quantidade)
    