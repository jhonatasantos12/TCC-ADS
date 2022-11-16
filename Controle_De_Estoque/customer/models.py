from django.db import models

# Create your models here.

class Customer(models.Model):
    nome = models.CharField(max_length=200)
    last_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    PhoneNumber = models.CharField(max_length=13)
    Dt_Nascimento = models.DateField()
    data_registro = models.DateTimeField(auto_now_add=True,null=True)