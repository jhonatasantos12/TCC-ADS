from django.urls import path
from . import views
urlpatterns = [
    path('StartPedido',views.pedidos, name ='StartPedido'),
    path('EntradaEstoque',views.entrada, name ='EntradaEstoque'),
    path('ListPedidos',views.Listadepedidos,name ='ListPedidos')
   
] 