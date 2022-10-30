from django.db import models
from django.forms import CharField
from pedidos.views import pedidos
from product import models as ProductModel
from customer import models as CustomerModel
from worker import models as WorkerModel
# Create your models here.

class Categoria(models.Model):
    description = models.CharField(max_length=125) 

class Pedido(models.Model):
    tp_Pedido = models.IntegerField(null=True) # 1 = Entrada 2 = Saida por Venda #3 = Saida por locação 
    Cliente = models.ForeignKey(CustomerModel.Customer,on_delete=models.PROTECT,null=True)
    Atendente = models.ForeignKey(WorkerModel.Worker,on_delete=models.PROTECT,null=True)
    Status = models.ForeignKey(Categoria,on_delete=models.PROTECT,null=True)
    data_registro = models.DateTimeField(auto_now_add=True)
    

class ProdutoPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    produto = models.ForeignKey(ProductModel.Product, on_delete=models.PROTECT)
    quantidade = models.IntegerField(null=False,default=0)
