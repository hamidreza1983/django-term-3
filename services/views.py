from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentsForm
from django.contrib import messages

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

    all_services = Paginator(all_service,2)
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
    #service = Services.objects.get(id=id)

    #service = get_object_or_404(Services, id=id)

    try:
        service = Services.objects.get(id=id)
        comments = Comments.objects.filter(product_name=service.name, status=True)
        service.counted_view += 1
        service.save()
        context = {
            'detail':service,
            'comments': comments,
        }
        return render(request, 'services/service-details.html', context = context)
    
    except:
        return render(request, 'services/404.html')


def qoute(request):
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your comments was delivered successfully and will be published ASAP !...')
            return redirect(request.path_info)
        else:
            messages.add_message(request, messages.ERROR, 'your input data may be incorrect')
            return redirect(request.path_info)
    else:
        return render(request, 'services/get-a-quote.html')
    
def edit_comment(request, id):
    comment = get_object_or_404(Comments, id=id)
    if request.method == 'POST':
        form = CommentsForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
#            obj = form.save(commit=False)
#            obj.status = False
#            obj.save()
            return redirect("services:services")
    else:
        form = CommentsForm(instance=comment)
        context = {
            'form': form,
        }
        return render (request, 'services/edit.html', context=context)
