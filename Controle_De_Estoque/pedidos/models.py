from django.db import models
from django.forms import CharField
from product import models as ProductModel
from customer import models as CustomerModel
from worker import models as WorkerModel
# Create your models here.

class Categoria(models.Model):
    description = models.CharField(max_length=125) 

class Pedido(models.Model):
    tp_Pedido = models.IntegerField(null=True) # 1 = Venda 2 = locação 
    Cliente = models.ForeignKey(CustomerModel.Customer,on_delete=models.CASCADE,null=True)
    Atendente = models.ForeignKey(WorkerModel.Worker,on_delete=models.CASCADE,null=True)
    Status = models.ForeignKey(Categoria,on_delete=models.CASCADE,null=True)
    data_registro = models.DateTimeField(auto_now_add=True)
    

class ProdutoPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(ProductModel.Product, on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=False,default=0)

class PedidoEntrada(models.Model):
    Atendente = models.ForeignKey(WorkerModel.Worker,on_delete=models.CASCADE,null=True)
    Status = models.ForeignKey(Categoria,on_delete=models.CASCADE,null=True)
    data_registro = models.DateTimeField(auto_now_add=True)
    

class ProdutoEntrada(models.Model):
    pedido = models.ForeignKey(PedidoEntrada, on_delete=models.CASCADE)
    produto = models.ForeignKey(ProductModel.Product, on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=False,default=0)