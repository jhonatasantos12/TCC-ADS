from django.contrib import admin
from .models import Pedido, ProdutoPedido, Categoria,PedidoEntrada , ProdutoEntrada
# Register your models here.
admin.site.register(Pedido, list_display=['Cliente', 'data_registro'])
admin.site.register(ProdutoPedido)
admin.site.register(Categoria)
admin.site.register(PedidoEntrada, list_display=['Atendente', 'data_registro'])
admin.site.register(ProdutoEntrada)