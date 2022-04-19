from django.contrib import admin
from .models import  Customer
# Register your models here.


class  CustomerAdmin(admin.ModelAdmin):
    list_display = ('nome','last_name','cpf','PhoneNumber','Dt_Nascimento')
    search_fields = ('nome','last_name','cpf','PhoneNumber','Dt_Nascimento')
    list_per_page = 10


admin.site.register(Customer,CustomerAdmin)