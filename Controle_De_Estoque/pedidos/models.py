from django.db import models
from django.forms import CharField
from pandas import notnull
from pedidos.views import pedidos
from product import models as ProductModel
from customer import models as CustomerModel
from worker import models as WorkerModel
# Create your models here.

class Pedido(models.Model):
    Categoria = models.BooleanField(default=True)#Padrão TRUE = Pedido / False = Entrada
    nr_pedido = models.IntegerField(null=True)
    Cliente = models.ForeignKey(CustomerModel.Customer,on_delete=models.PROTECT)
    Atendente = models.ForeignKey(WorkerModel.Worker,on_delete=models.PROTECT,null=True)
    Estoquista = models.CharField(max_length=255,null=True)
    Status = models.CharField(max_length=255)
    data_registro = models.DateTimeField(auto_now_add=True)

class ProdutoPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    produto = models.ForeignKey(ProductModel.Product, on_delete=models.PROTECT)
    quantidade = models.IntegerField(null=False,default=0)

