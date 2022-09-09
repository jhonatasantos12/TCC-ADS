from django.db import models
from product import models as ModelProduto
# Create your models here.

class Estoque(models.Model):
    produto = models.ForeignKey(ModelProduto.Product,on_delete=models.PROTECT)
    quantidade = models.IntegerField()
    min_prod = models.IntegerField(null=True,default=0)
    max_prod = models.IntegerField(null=True,default=0) 
