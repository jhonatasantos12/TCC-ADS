from django.forms import PasswordInput
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
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
        return render(request,'accounts/register.html',{
            'alert':alert
        })
    else:
        auth.login(request,user)
        return redirect('register')
def logout(request):
    auth.logout(request)
    return render(request,'accounts/logout.html')

def register(request):
    alert ={} 
    if request.method != 'POST': 
        return render(request,'accounts/register.html',{
        })
    email= request.POST.get('email')
    nome = request.POST.get('name')
    sobrenome = request.POST.get("last_name")
    cpf = request.POST.get('cpf')
    telefone = request.POST.get('PhoneNumber')
    cargo = request.POST.get('office')
    senha =request.POST.get('password') 
    senha_conf = request.POST.get('conf_password')
    if not sobrenome or not email or not nome or not cpf or not telefone or not cargo or not senha or not senha_conf:      
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
    user = User.objects.create_user(
        username=email,
        email=email,
        password=senha,
        first_name=nome,
        last_name=sobrenome)
    alert['type']=1 
    alert['title']="Sucesso" 
    alert['text']=f"{nome} Cadastrado com sucesso" 
    alert['icon']="success"
    return render(request,'accounts/register.html')