from django.db import models
from product import models as ModelProduto
# Create your models here.

class Estoque(models.Model):
    produto = models.ForeignKey(ModelProduto.Product,on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    min_prod = models.IntegerField(null=True,default=0)
    max_prod = models.IntegerField(null=True,default=0) 
    data_registro = models.DateTimeField(null=True,auto_now_add=True)
