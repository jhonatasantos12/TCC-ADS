from django.http import HttpResponse
from django.shortcuts import render
from pedidos.models import ProdutoPedido
from .models import Estoque as MEstoque 
from product import models as ModelProduto
from django.core.paginator import Paginator
from utils import functions
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
    try: 
        minInt = int(min)
        
    except:
        minInt = None
    try:
        maxInt = int(max)
        
    except:
        maxInt = None
    estoque = MEstoque.objects.get(id = estoque_id)
    if minInt and minInt < 0 :
            alert = functions.Alerts.alertError("erro","O min deve ser maior que zero")
            return render(request,'estoque/limites.html',context={'estoque': estoque,'alert':alert})
    if maxInt and maxInt<0:
            alert = functions.Alerts.alertError("erro","O max deve ser maior que zero")
            return render(request,'estoque/limites.html',context={'estoque': estoque,'alert':alert})
    if maxInt and minInt:
        if minInt >= maxInt:
            alert ={}
            alert['type']=1
            alert['title']="WARNING"
            alert['text']="O minimo não pode ser maior nem igual ao maximo"
            alert['icon']="error"
            return render(
                request, 
                'estoque/limites.html',
                context={
                    'estoque': estoque,
                    'alert': alert,
                }
            )

    if minInt:
        estoque.min_prod=min
    if maxInt:
        estoque.max_prod=max
    estoque.save()
    alert = functions.Alerts.alertSuccess('Succes','Alteração bem sucedida')
    return render(request,'estoque/limites.html',context={'estoque': estoque,'alert':alert})

def opcoes(request):
    return render(request,'estoque/opcoes.html')
