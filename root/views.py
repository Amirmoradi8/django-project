from django.shortcuts import render
from django.http import HttpResponse
from services.models import Specialservice

def home(request):
    return render(request , 'root/index.html' , context={'specials' : Specialservice.objects.all()})

def about(request):
    return render(request , 'root/about.html')

def contact(request):
    return render(request , 'root/contact.html')

# Create your views here.
