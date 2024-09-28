from django.urls import path
from .views import *

app_name = 'services'


urlpatterns = [
    path('' , services , name='services'),
    path('service-detail' , services_detail , name='services-detail'),
    path('quote/' , quote , name='quote'),
]
