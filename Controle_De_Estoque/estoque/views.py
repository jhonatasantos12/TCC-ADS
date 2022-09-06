from django.http import HttpResponse
from django.shortcuts import render
from .models import Estoque as MEstoque 
from .models import Limite as MLimite
from product import models as ModelProduto
# Create your views here.
def estoque(request):
    Estoque = MEstoque.objects.all()
    return render(
        request,
        'estoque/ListEstoque.html',
        context={
            'Estoque': Estoque,}
        ) 
def limite(request,prod_id):
    product = ModelProduto.Product.objects.get(id=prod_id)
    estoque = MEstoque.objects.get(produto= product)
    try:
        limite = MLimite.objects.get(id_estoque =estoque)
    except:
        limite = None
    return render(
        request,
        'estoque/limites.html',
        context={
            'estoque': estoque,
            'limites':limite,
        }
    )