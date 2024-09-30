from django.shortcuts import render
# from django.http import HttpResponse
from services.models import Specialservice
from .models import FrequentlyQuestions


def home(request):
    context = {
        'specials' : Specialservice.objects.filter(status=True)[:3],
        'questions' : FrequentlyQuestions.objects.filter(status=True)[:3]
        }
    return render(request , 'root/index.html' , context=context)

def about(request):
    return render(request , 'root/about.html')

def contact(request):
    return render(request , 'root/contact.html')

# Create your views here.
