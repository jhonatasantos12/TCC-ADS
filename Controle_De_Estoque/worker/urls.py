from django.urls import path
from . import views

urlpatterns = [
    path('ListWorker',views.ListWorker),
    path('EditWorker/<int:worker_id>',views.EditWorker),
    path('opcoes',views.opcoes),
]