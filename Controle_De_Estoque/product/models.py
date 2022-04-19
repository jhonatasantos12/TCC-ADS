from django.db import models
from django.utils import timezone
# Create your models here.


class Product(models.Model):
    nome = models.CharField(max_length=200)
    valor = models.FloatField()

    def GetAll(self):
        return  {
            'nome':self.nome,
            'valor':self.valor
        }
    

