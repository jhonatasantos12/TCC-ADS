from math import prod
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from flask import request
from product import models as ProductModel
from estoque import models as EstoqueModel
from customer import models as CustomerModel
# Create your views here.
def pedidos(request):
    if request.method !='POST':
        return render(request,'pedidos/StartPedido.html',
        context={
            "Customers": CustomerModel.Customer.objects.all(),
            "Estoque": EstoqueModel.Estoque.objects.all(),
        })
    cliente = request.POST.get('cliente')
    Estoque = EstoqueModel.Estoque.objects.all()
    ListaProd=[]
    for x in Estoque:
        try:
            produto = request.POST.get(str(x.produto.nome))
        except:
            produto = None
        if produto != None:
            ListaProd.append(produto)
        print(ListaProd,cliente,produto)
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
    