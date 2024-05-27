from django.shortcuts import render
from .models import SpecialService, Team, Skills , Category , Options , Services

# Create your views here.


def services(request):
    context = {
        "services" : Services.objects.filter(status=True),
        "special_services": SpecialService.objects.filter(status=True)
    }
    return render(request, 'services/services.html' , context = context)

def services_detail(request):
    return render(request, 'services/service-details.html')

def qoute(request):
    return render(request, 'services/get-a-quote.html')