from django.urls import path
from . import views
urlpatterns = [
    path('',views.opcoes),
    path('StartPedido',views.pedidos, name ='StartPedido'),
    path('EntradaEstoque',views.entrada, name ='EntradaEstoque'),
    path('ListPedidos',views.Listadepedidos,name ='ListPedidos'),
    path('PedidoNr/<int:pedido_id>',views.GetPedido),
    path('opcoes',views.opcoes),
   
] 