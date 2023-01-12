from django.urls import path

from services.views import get_services, create_services


urlpatterns = [
    path('get_services/', get_services),
    path('create_services/', create_services),
]