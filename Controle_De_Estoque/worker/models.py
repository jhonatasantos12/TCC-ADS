from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Worker(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE,
                                   verbose_name='Usuário',null=True)
    cpf = models.CharField(max_length=11)
    PhoneNumber = models.CharField(max_length=13)
    office = models.CharField(max_length=100)
    data_registro = models.DateTimeField(auto_now_add=True,null=True)
    def GetAll(self):
        return  {
            'cpf': self.cpf,
            'PhoneNumber':self.PhoneNumber,
            'office':self.office
        }