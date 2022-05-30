from django.db import models
from sqlalchemy import true
from product import models as ModelProduto
# Create your models here.

class Estoque(models.Model):
    produto = models.ForeignKey(ModelProduto.Product,on_delete=models.PROTECT)
    quantidade = models.IntegerField()
