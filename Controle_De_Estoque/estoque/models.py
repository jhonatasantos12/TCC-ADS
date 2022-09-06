from django.db import models
from product import models as ModelProduto
# Create your models here.

class Estoque(models.Model):
    produto = models.ForeignKey(ModelProduto.Product,on_delete=models.PROTECT)
    quantidade = models.IntegerField()

class min_max(models.Model):
    min_prod = models.IntegerField()
    max_prod = models.IntegerField() 
