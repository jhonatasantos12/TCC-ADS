from http.client import BAD_REQUEST
from django.http import Http404, JsonResponse
from django.shortcuts import render
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
# Create your views here.
@csrf_exempt
def AddProduct(request):
    if request.method != 'POST':
        return render(request,'product/AddProduct.html')
    nome = request.POST.get('product')
    valor = request.POST.get('value')
    if not nome or not valor:
        return Http404 

    if Product.objects.filter(nome= nome).exists():
        return Http404
    product = Product.objects.create(nome=nome,valor=valor)
    product.save()
    alert={}
    alert['type']=1
    alert['title']="Sucesso"
    alert['text']=f"{nome}, foi inserido com sucesso"
    alert['icon']="success"
    return render(
        request,
        'product/AddProduct.html',
        context={
            "alert": alert
            } 
        )

def ListProduct(request,):
    produtos = Product.objects.all()
    paginator = Paginator(produtos,5)
    page = request.GET.get("produtos")
    produtos = paginator.get_page(page)
    return render(request,'product/ListProduct.html',{'Products':produtos})

def EditProduct(request,product_id):
    product = Product.objects.get(id = product_id)
    if request.method != 'POST': 
        return render(request,'product/EditProduct.html',{
            'resultado':product
        })    
    nome = request.POST.get('product')
    valor = request.POST.get('value')
    if not nome or not valor:
        return Http404 
    product.nome = nome
    product.valor = valor
    product.save()
    alert={}
    alert['type']=1
    alert['title']="Sucesso"
    alert['text']=f"{nome}, foi editado com sucesso"
    alert['icon']="success"
    return render(
        request,
        'product/EditProduct.html',
        context={
            "alert": alert,
            'resultado':product
            } 
        )
        
          
def GetProduct(request):
    lista =[]
    product = Product.objects.all()
    for x in product:
        dict ={}
        dict['id'] = x.id
        dict['nome'] = x.nome
        lista.append(dict)
    return JsonResponse({'dict':lista})
def opcoes(request):
    return render(request,'product/opcoes.html')