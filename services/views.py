from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentsForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, RedirectView

# Create your views here.



class ServiceView(ListView):
    template_name = 'services/services.html'
    context_object_name = 'services'
    # queryset = Services.objects.filter(status=True)
    #paginate_by = 2

    def get_queryset(self):

        if self.kwargs.get ('category'):
            all_service = Services.objects.filter(category__title=self.kwargs.get('category'))
        else:
            all_service = Services.objects.filter(status=True)
        
        return all_service



class GoogleView(RedirectView):
    url = "https://google.com"

class ServiceDetaiView(DetailView):
    model = Services
    template_name = 'services/service-details.html'
    context_object_name = 'detail'


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        service = Services.objects.get(pk=self.kwargs.get("pk"))
        commnets = Comments.objects.filter(product_name=service.name, status=True)
        context ['comments'] = commnets
        return context


# def services(request, **kwargs):
# #    if request.GET.get('category') is not None:
# #        all_service = Services.objects.filter(category__title=request.GET.get('category'))
#     if kwargs.get('category'):
#         all_service = Services.objects.filter(category__title=kwargs.get('category'))

        
#     elif request.GET.get('search') is not None:
#         all_service = Services.objects.filter(content__contains=request.GET.get('search'))

# #    elif price:
# #        all_service = Services.objects.filter(price__lte=price)
#     elif kwargs.get('price'):
#         all_service = Services.objects.filter(price__lte=kwargs.get('price'))

#     else:
#         all_service = Services.objects.filter(status=True)

#     all_services = Paginator(all_service,2)
#     last_page = all_services.num_pages
#     try:
#         page_number = request.GET.get('page')
#         all_services = all_services.get_page(page_number)
#     except PageNotAnInteger:
#         all_services = all_services.get_page(1)
#     except EmptyPage:
#          all_services = all_services.get_page(1)
#Comments.objects.filter(product_name=service.name, status=True)
#             "specials": SpecialService.objects.filter(status=True),
#             'last_page': last_page,
#         }
#     return render(request, 'services/services.html', context = context)



# def services_detail(request, id):
#     #service = Services.objects.get(id=id)

#     #service = get_object_or_404(Services, id=id)

#     try:
#         service = Services.objects.get(id=id)
#         comments = Comments.objects.filter(product_name=service.name, status=True)
#         service.counted_view += 1
#         service.save()
#         context = {
#             'detail':service,
#             'comments': comments,
#         }
#         return render(request, 'services/service-details.html', context = context)
    
#     except:
#         return render(request, 'services/404.html')


def qoute(request):
    if request.method == 'POST':
        #if request.user.is_authenticated:
            form = CommentsForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'your comments was delivered successfully and will be published ASAP !...')
                return redirect(request.path_info)
            else:
                messages.add_message(request, messages.ERROR, 'your input data may be incorrect')
                return redirect(request.path_info)
        # else:
        #     return redirect('accounts:login')
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
