from django.urls import path
from . import views
urlpatterns = [
    path('AddProduct',views.AddProduct, name ='AddProduct'),
    path('ListProduct',views.ListProduct,name='ListProduct'),
    path('EditProduct/<int:product_id>',views.EditProduct,name='EditProduct'),
    path('api/GetProduct',views.GetProduct, name='GetProduct'),
    path('opcoes',views.opcoes)
] 