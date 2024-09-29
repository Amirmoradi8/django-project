from django.urls import path
from .views import *

app_name = 'services'


urlpatterns = [
    path('' , services , name='services'),
    path('service-details' , services_details , name='services-details'),
    path('quote/' , quote , name='quote'),
]
