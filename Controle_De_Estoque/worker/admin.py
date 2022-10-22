from django.contrib import admin

# Register your models here.
from .models import  Worker

class  WorkerAdmin(admin.ModelAdmin):
    list_display = ('cpf','PhoneNumber','office')
    search_fields = ('cpf','PhoneNumber','office')
    list_per_page = 10


admin.site.register(Worker,WorkerAdmin)