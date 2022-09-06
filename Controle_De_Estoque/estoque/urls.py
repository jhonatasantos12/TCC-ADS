from django.urls import path
from . import views
urlpatterns = [
    path('estoque',views.estoque, name ='estoque'),
    path('limite/<int:prod_id>',views.limite, name='limite'),
] 