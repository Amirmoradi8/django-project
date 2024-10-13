from django.shortcuts import render
# from django.http import HttpResponse
from services.models import Specialservice
from .models import FrequentlyQuestions
from services.models import Team
# from services.models import Skills


def home(request):

    context = {
        'specials' : Specialservice.objects.filter(status=True)[:3],
        'questions' : FrequentlyQuestions.objects.filter(status=True)[:3],
        'team' : Team.objects.filter(status=True)[:3],
        # 'team' : Team.objects.filter(skills__title = 'sk1'),
        }
    return render(request , 'root/index.html' , context=context)

def about(request):

    context = {
        'team' : Team.objects.filter(status=True),
        }
    return render(request , 'root/about.html' , context=context)

def contact(request):
    return render(request , 'root/contact.html')

# Create your views here.
