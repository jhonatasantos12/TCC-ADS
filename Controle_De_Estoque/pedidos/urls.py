from django.urls import path
from . import views

urlpatterns = [
    path('',views.opcoes),
    path('ListPedidos',views.Listadepedidos,name ='ListPedidos'),
    path('PedidoNr/<int:pedido_id>',views.GetPedido),
    path('opcoes',views.opcoes),
    path('gerarEntrada',views.GerarEntrada, name='GerarEntrada'),
    path('gerarPedido',views.GerarPedido, name ="GerarPedido"),
    path('listaEntrada',views.listaEntrada, name ="listaEntrada"),
    path('Detalhes/<int:pedido_id>',views.EntradaDetalhes),
    path('sempermisao',views.SemPermisao,name='sempermisao')
   
] 