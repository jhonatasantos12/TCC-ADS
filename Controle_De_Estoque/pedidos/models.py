from django.db import models
from django.forms import CharField
from pedidos.views import pedidos
from product import models as ProductModel
from customer import models as CustomerModel
from worker import models as WorkerModel
# Create your models here.

class Categoria(models.Model):
    status = models.CharField(max_length=125) 

class Pedido(models.Model):
    
    nr_pedido = models.IntegerField(null=True)
    Cliente = models.ForeignKey(CustomerModel.Customer,on_delete=models.PROTECT)
    Atendente = models.ForeignKey(WorkerModel.Worker,on_delete=models.PROTECT,null=True)
    Estoquista = models.CharField(max_length=255,null=True)
    #Status = models.CharField(max_length=125) 
    Status = models.ForeignKey(Categoria,on_delete=models.PROTECT,null=True)
    
    data_registro = models.DateTimeField(auto_now_add=True)
    

class ProdutoPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    produto = models.ForeignKey(ProductModel.Product, on_delete=models.PROTECT)
    quantidade = models.IntegerField(null=False,default=0)
