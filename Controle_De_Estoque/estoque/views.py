from django.http import HttpResponse
from django.shortcuts import render
from .models import Estoque as MEstoque
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
    product = MEstoque.objects.get(produto.id = prod_id)

    return render(
        request,
        'estoque/limites.html',
        context={
            'context': product,
        }
    )