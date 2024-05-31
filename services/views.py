from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def services(request, **kwargs):
#    if request.GET.get('category') is not None:
#        all_service = Services.objects.filter(category__title=request.GET.get('category'))
    if kwargs.get('category'):
        all_service = Services.objects.filter(category__title=kwargs.get('category'))

        
    elif request.GET.get('search') is not None:
        all_service = Services.objects.filter(content__contains=request.GET.get('search'))

#    elif price:
#        all_service = Services.objects.filter(price__lte=price)
    elif kwargs.get('price'):
        all_service = Services.objects.filter(price__lte=kwargs.get('price'))

    else:
        all_service = Services.objects.filter(status=True)

    all_services = Paginator(all_service,1)
    last_page = all_services.num_pages
    try:
        page_number = request.GET.get('page')
        all_services = all_services.get_page(page_number)
    except PageNotAnInteger:
        all_services = all_services.get_page(1)
    except EmptyPage:
         all_services = all_services.get_page(1)




    context = {
            "services": all_services,
            "specials": SpecialService.objects.filter(status=True),
            'last_page': last_page,
        }
    return render(request, 'services/services.html', context = context)

def services_detail(request, id):
    service = Services.objects.get(id=id)

    context = {
        'detail':service,
    }
    return render(request, 'services/service-details.html', context = context)

def qoute(request):
    return render(request, 'services/get-a-quote.html')