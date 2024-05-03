from django.shortcuts import render

# Create your views here.


def services(request):
    return render(request, 'services/services.html')

def services_detail(request):
    return render(request, 'services/service-details.html')

def qoute(request):
    return render(request, 'services/get-a-quote.html')