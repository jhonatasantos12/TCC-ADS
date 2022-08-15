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