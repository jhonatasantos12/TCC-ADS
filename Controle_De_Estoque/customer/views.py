from attr import validate
from django.http import  JsonResponse
from django.shortcuts import render
from .models import Customer
from django.core.paginator import Paginator
from utils.functions import validate_cpf
from utils import functions
import datetime 


# Create your views here.
def AddCustomer(request):
    if request.method != 'POST':
        return render(request,'customer/AddCustomer.html')
    nome = request.POST.get('name')
    sobrenome = request.POST.get('last_name')
    cpf = request.POST.get('cpf')
    telefone = request.POST.get('phoneNumber')
    Dt_Nascimento = request.POST.get('bdaytime')
    
    hoje = datetime.date.today()
    hoje = hoje.strftime('%d/%m/%Y')
    
    anoatual = hoje[6:10]
    mesatual = hoje[3:5]
    diaatual=  hoje[0:2]
    anonascimento= Dt_Nascimento[0:4]
    mesnascimento= Dt_Nascimento[5:7]
    dianascimento= Dt_Nascimento[8:10]
    if int(anoatual)<int(anonascimento):
        alert = functions.Alerts.alertError("Erro","A data deve ser anterior a hoje")
        return render(request, 'customer/AddCustomer.html', context={ "alert": alert})
    if int(anoatual)==int(anonascimento):
        if int(mesatual)<int(mesnascimento):
            alert = functions.Alerts.alertError("Erro","A data deve ser anterior a hoje")
            return render(request, 'customer/AddCustomer.html', context={ "alert": alert})
        if int(mesatual)==int(mesnascimento):
            if int(diaatual)<int(dianascimento):
                alert = functions.Alerts.alertError("Erro","A data deve ser anterior a hoje")
                return render(request, 'customer/AddCustomer.html', context={ "alert": alert})
    validatecpf = validate_cpf(cpf)
    if validatecpf == False:
        alert = functions.Alerts.alertError("Erro","Digite um CPF valido")
        return render( request,'customer/AddCustomer.html', context={"alert": alert})  
    if Customer.objects.filter(cpf = cpf ).exists():
        alert = functions.Alerts.alertError("Erro","Já existe um cliente cadastrado com esse CPF")
        return render(request, 'customer/AddCustomer.html', context={ "alert": alert}) 
    
    
         
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
    hoje = datetime.date.today()
    hoje = hoje.strftime('%d/%m/%Y')
    
    anoatual = hoje[6:10]
    mesatual = hoje[3:5]
    diaatual=  hoje[0:2]
    anonascimento= Dt_Nascimento[0:4]
    mesnascimento= Dt_Nascimento[5:7]
    dianascimento= Dt_Nascimento[8:10]
    if int(anoatual)<int(anonascimento):
        alert = functions.Alerts.alertError("Erro","A data deve ser anterior a hoje")
        return render(request,'customer/EditCustomer.html',context={'alert': alert,'resultado':customer,})
    if int(anoatual)==int(anonascimento):
        if int(mesatual)<int(mesnascimento):
            alert = functions.Alerts.alertError("Erro","A data deve ser anterior a hoje")
            return render(request,'customer/EditCustomer.html',context={'alert': alert,'resultado':customer,})
        if int(mesatual)==int(mesnascimento):
            if int(diaatual)<int(dianascimento):
                alert = functions.Alerts.alertError("Erro","A data deve ser anterior a hoje")
                return render(request,'customer/EditCustomer.html',context={'alert': alert,'resultado':customer,})
    customer.nome = nome
    customer.last_name = sobrenome
    customer.cpf = cpf
    customer.PhoneNumber = telefone
    customer.Dt_Nascimento = Dt_Nascimento
    customer.save()
    alert={}
    alert['type']=1
    alert['title']="Sucesso"
    alert['text']=f"{nome}, foi editado com sucesso"
    alert['icon']="success"
    customer = Customer.objects.get(id = customer_id)
    return render(request,'customer/EditCustomer.html',context={'alert': alert,'resultado':customer,})

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
