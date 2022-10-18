from django.http import Http404
from django.shortcuts import render
import worker
from .models import Worker
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def AddWorker(request):
    if request.method != 'POST':
        return render(request,'worker/AddWorker.html')
    nome = request.POST.get('name')
    sobrenome = request.POST.get('last_name')
    cpf = request.POST.get('cpf')
    telefone = request.POST.get('PhoneNumber')
    cargo = request.POST.get('office')

    if Worker.objects.filter(cpf = cpf ).exists():
        return Http404
    Trabalhador = Worker.objects.create(nome = nome,last_name=sobrenome,cpf=  cpf ,PhoneNumber = telefone, office = cargo)
    Trabalhador.save()
    alert={}
    alert['type']=1
    alert['title']="Sucesso"
    alert['text']=f"{nome}, foi cadastrado com sucesso"
    alert['icon']="success"
    return render(
        request,
        'worker/AddWorker.html',
        context={
            'alert': alert
            }
            )

def ListWorker(request):
    Workers = Worker.objects.all()
    return render(request,'worker/ListWorker.html',{'Workers': Workers})


def EditWorker(request,worker_id):
    worker = Worker.objects.get(id = worker_id)
    if request.method != 'POST': 
        return render(request,'worker/EditWorker.html',{
        'resultado':worker
        })
    nome = request.POST.get('name')
    sobrenome = request.POST.get('last_name')
    cpf = request.POST.get('cpf')
    telefone = request.POST.get('PhoneNumber')
    cargo = request.POST.get('office')
    worker.nome = nome 
    worker.last_name = sobrenome
    worker.cpf = cpf
    worker.PhoneNumber= telefone
    worker.office = cargo 
    worker.save()
    alert = {}
    alert['type']=1
    alert['title']="Sucesso"
    alert['text']=f"{nome}, foi editado com sucesso"
    alert['icon']="success"
    return render(
        request,
        'worker/EditWorker.html',
        context={
            'alert': alert,
            'resultado':worker
        }
        )
def opcoes(request):
    return render(request,'worker/opcoes.html')