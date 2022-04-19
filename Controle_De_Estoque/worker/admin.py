from django.contrib import admin

# Register your models here.
from .models import  Worker

class  WorkerAdmin(admin.ModelAdmin):
    list_display = ('nome','last_name','cpf','PhoneNumber','office')
    search_fields = ('nome','last_name','cpf','PhoneNumber','office')
    list_per_page = 10


admin.site.register(Worker,WorkerAdmin)