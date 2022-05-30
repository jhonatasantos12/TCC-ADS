from django.db import models
from django.forms import CharField
from pedidos.views import pedidos
from product import models as ProductModel
from customer import models as CustomerModel
from worker import models as WorkerModel
# Create your models here.

class Pedido(models.Model):
    Catagoria = models.BooleanField(default=True)#Padrão TRUE = Pedido / False = Entrada
    nr_pedido = models.IntegerField(unique=True)
    Cliente = models.ForeignKey(CustomerModel.Customer,on_delete=models.PROTECT)
    Atendete = models.ForeignKey(WorkerModel.Worker,on_delete=models.PROTECT)
    Estoquista = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)
    data_registro = models.DateField()
    
class ProdutoPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    produto = models.ForeignKey(ProductModel.Product, on_delete=models.PROTECT)
