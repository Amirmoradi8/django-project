from django.shortcuts import render

# Create your views here.

def services(request):
    return render(request , 'services/services.html')

def services_details(request):
    return render(request , 'services/service-details.html')

def quote(request):
    return render(request , 'services/get-a-quote.html')
