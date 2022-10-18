from django.urls import path
from . import views

urlpatterns = [
    path('AddWorker',views.AddWorker, name='AddWorker'),
    path('ListWorker',views.ListWorker),
    path('EditWorker/<int:worker_id>',views.EditWorker),
    path('opcoes',views.opcoes),
]