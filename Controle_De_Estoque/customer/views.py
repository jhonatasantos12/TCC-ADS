from django.http import Http404, JsonResponse
from django.shortcuts import render
from .models import Customer

# Create your views here.
def AddCustomer(request):
    if request.method != 'POST':
        return render(request,'customer/AddCustomer.html')
    nome = request.POST.get('name')
    sobrenome = request.POST.get('last_name')
    cpf = request.POST.get('cpf')
    telefone = request.POST.get('PhoneNumber')
    Dt_Nascimento = request.POST.get('bdaytime')

    if Customer.objects.filter(cpf = cpf ).exists():
        return Http404
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
    return render(request,'customer/EditCustomer.html',{
            'resultado':customer
            })
def ListCustomer(request):
    customers = Customer.objects.all()
    return render(request,'customer/ListCustomer.html', {'resultado':customers})
    
def GetAll(request):
    lista =[]
    customers = Customer.objects.all()
    for x in customers:
        dict ={}
        dict['nome'] = x.nome
        dict['last_name'] = x.last_name
        dict['cpf'] = x.cpf
        #dict['PhoneNumber'] = x.PhoneNumber
        #dict['Dt_Nascimento'] = x.Dt_Nascimento
        lista.append(dict)
    return JsonResponse({'dict':lista})    
