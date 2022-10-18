from django.urls import path
from . import views

urlpatterns = [
    path('AddCustomer',views.AddCustomer,name='AddCustomer'),
    path('EditCustomer/<int:customer_id>',views.EditCustomer,name='EditCustomer'),
    path('ListCustomer',views.ListCustomer,name='ListCustomer'),
    path('api/GetAll',views.GetAll),
    path('opcoes',views.opcoes)
]
