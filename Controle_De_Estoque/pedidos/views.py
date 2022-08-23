from math import prod
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from product import models as ProductModel
from estoque import models as EstoqueModel
from customer import models as CustomerModel
from pedidos import models as PedidosModel
from datetime import datetime
# Create your views here.


def GetPedido(request,pedido_id):
    if request.method !='POST':
        Pedido = PedidosModel.Pedido.objects.get(id= pedido_id)
        ProdutosPedido = PedidosModel.ProdutoPedido.objects.filter(pedido = Pedido)
        if Pedido.Status.description == "Finalizado" or Pedido.Status.description == "Cancelado":
            alternable = False
        else:
            alternable = True
        #Categoria = PedidosModel.Categoria.objects.all()
        return render(request,'pedidos/PedidoGerado.html',
        context={
        'Pedido':Pedido,
        'ProdutosPedido':ProdutosPedido,
        'Categoria' :PedidosModel.Categoria.objects.all() ,
        'IsAlternable' : alternable,
        }) 
    status = request.POST.get('newStatus')
    pedido = PedidosModel.Pedido.objects.get(id= pedido_id)
    categoria = PedidosModel.Categoria.objects.get(id=status)
    pedido.Status = categoria
    pedido.save()
    Pedido = PedidosModel.Pedido.objects.get(id= pedido_id)
    ProdutosPedido = PedidosModel.ProdutoPedido.objects.filter(pedido = Pedido)
    if Pedido.Status.description == "Finalizado" or Pedido.Status.description == "Cancelado":
        alternable = False
    else:
        alternable = True
    return render(request,'pedidos/PedidoGerado.html',
        context={
        'Pedido':Pedido,
        'ProdutosPedido':ProdutosPedido,
        'Categoria' :PedidosModel.Categoria.objects.all() ,
        'IsAlternable' : alternable,
        }) 



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
            if int(produto) > limiteEstq.quantidade:
                return HttpResponse('Quantidade informada Indisponivel')
            ProdPedido['Produtos'][str(x.produto.id)] = {}
            ProdPedido['Produtos'][str(x.produto.id)]['Id'] = str(x.produto.id)
            ProdPedido['Produtos'][str(x.produto.id)]['NameProduct'] = str(x.produto.nome)
            ProdPedido['Produtos'][str(x.produto.id)]['Quantidade'] = produto
    if  ProdPedido['Produtos']:
        ProdPedido['Cliente'] =  cliente
        ProdPedido['Status'] = "Em Separação"
    else:
        print("Num tem produto bixo")
    Pcliente = CustomerModel.Customer.objects.get(id = ProdPedido['Cliente'])
    status = PedidosModel.Categoria.objects.get(id = 1)
    pedido = PedidosModel.Pedido.objects.create(Cliente = Pcliente, Status= status)
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

def opcoes(request):
    return render(request,'pedidos/opcoes.html')

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
    