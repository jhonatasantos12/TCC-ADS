from django.db import models
from django.utils import timezone
# Create your models here.


class Product(models.Model):
    nome = models.CharField(max_length=200)
    valor = models.FloatField()
    data_registro = models.DateTimeField(auto_now_add=True)
    def GetAll(self):
        return  {
            'nome':self.nome,
            'valor':self.valor
        }
    

