from django.http import HttpResponse
from django.shortcuts import render
from pedidos.models import ProdutoPedido
from .models import Estoque as MEstoque 
from product import models as ModelProduto
from django.core.paginator import Paginator

# Create your views here.
def estoque(request):
    Estoque = MEstoque.objects.all()
    paginator = Paginator(Estoque,5)
    page = request.GET.get("estoque")
    Estoque = paginator.get_page(page)
    return render(
        request,
        'estoque/ListEstoque.html',
        context={
            'Estoque': Estoque,
            }
        ) 
def limite(request,estoque_id):
    if request.method != 'POST': 
        estoque = MEstoque.objects.get(id = estoque_id)
        return render(
            request,
            'estoque/limites.html',
            context={
                'estoque': estoque,
            }
        )
    min = request.POST.get('min_prod')
    max = request.POST.get('max_prod')
    minInt = int(min)
    maxInt = int(max)
    estoque = MEstoque.objects.get(id = estoque_id)
    if minInt > maxInt:
        alert ={}
        alert['type']=1
        alert['title']="WARNING"
        alert['text']="O minimo não pode ser maior que o maximo"
        alert['icon']="error"
        return render(
            request, 
            'estoque/limites.html',
            context={
                'estoque': estoque,
                'alert': alert,
            }
        )
    estoque.min_prod=min
    estoque.max_prod=max
    estoque.save()
    return render(
            request,
            'estoque/limites.html',
            context={
                'estoque': estoque,
            }
        )

def opcoes(request):
    return render(request,'estoque/opcoes.html')
