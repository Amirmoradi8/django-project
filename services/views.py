from django.shortcuts import render
from .models import *

# Create your views here.

def services(request):
    context = {
        'services' : Service.objects.filter(status=True),
        'specials' : Specialservice.objects.filter(status=True)
    }
    return render(request , 'services/services.html' , context = context)

def services_details(request):
    return render(request , 'services/service-details.html')

def quote(request):
    return render(request , 'services/get-a-quote.html')
