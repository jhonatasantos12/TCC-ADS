from django.contrib import admin
from .models import Pedido, ProdutoPedido
# Register your models here.
admin.site.register(Pedido, list_display=['Cliente', 'data_registro'])
admin.site.register(ProdutoPedido)