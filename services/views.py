from django.shortcuts import render
from .models import Service
from .models import Specialservice

# Create your views here.

# def services(request):
def services(request , *args , **kwargs):

    if kwargs.get('category'):
        services = Service.objects.filter(category__title=kwargs.get('category'))

def services(request , category=None):
    # if category:
        # all_service = Service.objects.filter(category__title=category)
        # if request.GET.get('category') is not None:
        if category:
        # all_service = Service.objects.filter(category__title=request.GET.get('category'))
            context = {
            # 'services' : Service.objects.filter(category__title=request.GET.get('category')),
            'services' : Service.objects.filter(category__title=category),
            'specials' : Specialservice.objects.filter(status=True),
        }
        elif request.GET.get('search') is not None:
        # all_service = Service.objects.filter(content__contains=request.GET.get('search'))
            context = {
            'services' : Service.objects.filter(content__contains=request.GET.get('search')),
            'specials' : Specialservice.objects.filter(status=True),
        }
        elif request.GET.get('price') is not None:
        # all_service = Service.objects.filter(price__lte=request.GET.get('price'))
            context = {
                'services' : Service.objects.filter(price__lte=request.GET.get('price')),
                'specials' : Specialservice.objects.filter(status=True)
            }
        else:
        # all_service = Specialservice.objects.filter(status=True)
            context = {
            'services' : Service.objects.filter(status=True),
            'specials' : Specialservice.objects.filter(status=True)
            }
        return render(request , 'services/services.html' , context = context)

def services_details(request):
    return render(request , 'services/service-details.html')

def quote(request):
    return render(request , 'services/get-a-quote.html')
