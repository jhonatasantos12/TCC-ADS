from attr import validate
from django.http import  JsonResponse
from django.shortcuts import render
from .models import Customer
from django.core.paginator import Paginator
from utils.functions import validate_cpf
from utils import functions

# Create your views here.
def AddCustomer(request):
    if request.method != 'POST':
        return render(request,'customer/AddCustomer.html')
    nome = request.POST.get('name')
    sobrenome = request.POST.get('last_name')
    cpf = request.POST.get('cpf')
    telefone = request.POST.get('phoneNumber')
    Dt_Nascimento = request.POST.get('bdaytime')
    validatecpf = validate_cpf(cpf)
    if validatecpf == False:
        alert = functions.Alerts.alertError("Erro","Digite um CPF valido")
        return render(
        request,
        'customer/AddCustomer.html',
        context={
            "alert": alert
            }
        )  
    if Customer.objects.filter(cpf = cpf ).exists():
        alert = functions.Alerts.alertError("Erro","Já existe um cliente cadastrado com esse CPF")
        return render(
        request,
        'customer/AddCustomer.html',
        context={
            "alert": alert
            }
        )  
    Cliente = Customer.objects.create(nome = nome,last_name=sobrenome,cpf=  cpf ,PhoneNumber = telefone, Dt_Nascimento = Dt_Nascimento)
    Cliente.save()
    alert={}
    alert['type']=1
    alert['title']="Sucesso"
    alert['text']=f"{nome} {sobrenome}, Cadastrado(a) com sucesso"
    alert['icon']="success"
    return render(
        request,
        'customer/AddCustomer.html',
        context={
            "alert": alert
            }
        )
    
def EditCustomer(request,customer_id):
    customer = Customer.objects.get(id = customer_id)
    if request.method != 'POST': 
        return   render(request,'customer/EditCustomer.html',{
            'resultado':customer
            })
    nome = request.POST.get('name')
    sobrenome = request.POST.get('last_name')
    cpf = request.POST.get('cpf')
    telefone = request.POST.get('PhoneNumber')
    Dt_Nascimento = request.POST.get('bdaytime')
    customer.nome = nome
    customer.last_name = sobrenome
    customer.cpf = cpf
    customer.PhoneNumber = telefone
    if Dt_Nascimento != None:
        customer.Dt_Nascimento = Dt_Nascimento
    customer.save()
    alert={}
    alert['type']=1
    alert['title']="Sucesso"
    alert['text']=f"{nome}, foi editado com sucesso"
    alert['icon']="success"
    return render(
        request,
        'customer/EditCustomer.html',
        context={
            'alert': alert,
            'resultado':customer
            }
            )
def ListCustomer(request):
    customers = Customer.objects.all()
    paginator = Paginator(customers,5)
    page = request.GET.get("cliente")
    customers = paginator.get_page(page)
    return render(request,'customer/ListCustomer.html', {'customers':customers})
    
def GetAll(request):
    lista =[]
    customers = Customer.objects.all()
    for x in customers:
        dict ={}
        dict['nome'] = x.nome
        dict['last_name'] = x.last_name
        dict['cpf'] = x.cpf
        lista.append(dict)
    return JsonResponse({'dict':lista})    
def opcoes(request):
    return render(request,'customer/opcoes.html')
