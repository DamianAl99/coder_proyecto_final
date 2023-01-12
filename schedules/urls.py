from django.urls import path

from schedules.views import get_schedules, create_schedules


urlpatterns = [
    path('get_schedules/', get_schedules),
    path('create_schedules/', create_schedules),
]