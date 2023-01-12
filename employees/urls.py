from django.urls import path

from employees.views import get_clientes, create_clients


urlpatterns = [
    path('get_employees/', get_clientes),
    path('create_employees/', create_clients),
]