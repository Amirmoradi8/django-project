from django.http import HttpResponse

from django.urls import path
from .views import *

urlpatterns = [
    path('' , home),
    path('about/' , about),
    path('contact/' , contact),
]
