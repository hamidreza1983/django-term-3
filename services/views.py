from django.shortcuts import render
from .models import *

# Create your views here.


def services(request, category=None):
#    if request.GET.get('category') is not None:
#        all_service = Services.objects.filter(category__title=request.GET.get('category'))
    if category:
        all_service = Services.objects.filter(category__title=category)

        
    elif request.GET.get('search') is not None:
        all_service = Services.objects.filter(content__contains=request.GET.get('search'))

    elif request.GET.get('price') is not None:
        all_service = Services.objects.filter(price__lte=request.GET.get('price'))

    else:
        all_service = Services.objects.filter(status=True)


    context = {
            "services": all_service,
            "specials": SpecialService.objects.filter(status=True)
        }
    return render(request, 'services/services.html', context = context)

def services_detail(request):
    return render(request, 'services/service-details.html')

def qoute(request):
    return render(request, 'services/get-a-quote.html')