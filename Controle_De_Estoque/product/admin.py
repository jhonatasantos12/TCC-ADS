from django.contrib import admin
from .models import  Product
# Register your models here.




class  ProductAdmin(admin.ModelAdmin):
    list_display = ('nome','valor')
    search_fields = ('nome','valor')
    list_per_page = 10
    
    

admin.site.register(Product,ProductAdmin)