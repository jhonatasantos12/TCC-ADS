from django.forms import PasswordInput
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from worker import models as  WorkerModel
# Create your views here.


def login(request):
    alert ={} 
    if request.method != 'POST': 
        return render(request,'accounts/login.html',{
        })
    
    login= request.POST.get('login')
    senha = request.POST.get('password')
    user = auth.authenticate(request, username=login,password=senha)

    if not user :
        alert['type']=1 
        alert['title']="Erro" 
        alert['text']="Usuário ou senha invalido" 
        alert['icon']="error" 
        return render(request,'accounts/login.html',{
            'alert':alert
        })
    else:
        auth.login(request,user)
        return redirect('pedidos/opcoes')
def logout(request):
    auth.logout(request)
    return redirect('register')

def register(request):
    alert ={} 
    if request.method != 'POST': 
        return render(request,'accounts/register.html',{
        })
    email= request.POST.get('email')
    usuario = request.POST.get("user")
    nome = request.POST.get('name')
    sobrenome = request.POST.get("last_name")
    cpf = request.POST.get('cpf')
    telefone = request.POST.get('PhoneNumber')
    cargo = request.POST.get('office')
    senha =request.POST.get('password') 
    senha2 = request.POST.get('conf_password')
    
    if not sobrenome or not email or not nome or not cpf or not telefone or not cargo or not senha or not senha2:      
        alert['type']=1 
        alert['title']="Erro" 
        alert['text']="Nenhum campo pode estar vazio" 
        alert['icon']="error" 
        return render(request,'accounts/register.html',{
            'alert':alert
        })
    try:
        validate_email(email)
    except:
        alert['type']=1 
        alert['title']="Erro" 
        alert['text']="Email invalido" 
        alert['icon']="error" 
        return render(request,'accounts/register.html',{
            'alert':alert
        })
    if len(senha) < 6:
        alert['type']=1 
        alert['title']="Erro" 
        alert['text']="A senha precisa ter 6 caracteres ou mais" 
        alert['icon']="error" 
        return render(request, 'accounts/register.html',{'alert':alert})

    if len(usuario) < 6:
        alert['type']=1 
        alert['title']="Erro" 
        alert['text']="Usuário precisa ter 6 caracteres ou mais" 
        alert['icon']="error" 
        return render(request, 'accounts/register.html',{'alert':alert})

    if senha != senha2:
        alert['type']=1 
        alert['title']="Erro" 
        alert['text']="Senhas não conferem." 
        alert['icon']="error" 
        return render(request, 'accounts/register.html',{'alert':alert})

    if User.objects.filter(username=usuario).exists():
        alert['type']=1 
        alert['title']="Erro" 
        alert['text']="Usuário já existe." 
        alert['icon']="error" 
        return render(request, 'accounts/register.html',{'alert':alert})

    if User.objects.filter(email=email).exists():
        alert['type']=1 
        alert['title']="Erro" 
        alert['text']="Email já existe." 
        alert['icon']="error" 
        return render(request, 'accounts/register.html',{'alert':alert})
    if WorkerModel.Worker.objects.filter(cpf = cpf ).exists():
        alert['type']=1 
        alert['title']="Erro" 
        alert['text']="CPF já existe." 
        alert['icon']="error" 
        return render(request, 'accounts/register.html',{'alert':alert})

     
    user = User.objects.create_user(
        username=usuario,
        email=email,
        password=senha,
        first_name=nome,
        last_name=sobrenome)
    alert['type']=1 
    alert['title']="Sucesso" 
    alert['text']=f"{nome} Cadastrado com sucesso" 
    alert['icon']="success"
    funcionario = WorkerModel.Worker.objects.create(usuario = user,cpf=  cpf ,PhoneNumber = telefone, office = cargo)
    funcionario.save   
    return render(request,'')