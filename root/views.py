from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request , 'root/index.html')

def about(request):
    return render(request , 'root/about.html')

def contact(request):
    return render(request , 'root/contact.html')

# Create your views here.
