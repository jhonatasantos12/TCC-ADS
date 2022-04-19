from django.db import models

# Create your models here.


    
class Worker(models.Model):
    nome = models.CharField(max_length=200)
    last_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    PhoneNumber = models.CharField(max_length=13)
    office = models.CharField(max_length=100)
    
    def GetAll(self):
        return  {
            'nome':self.nome,
            'last_name':self.last_name,
            'cpf': self.cpf,
            'PhoneNumber':self.PhoneNumber,
            'office':self.office
        }