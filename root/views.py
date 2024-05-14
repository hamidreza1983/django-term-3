from django.shortcuts import render
from services.models import SpecialService
from .models import FrequentlyQuestions


from django.http import HttpResponse


def home(request):

    context = {
        'specials': SpecialService.objects.filter(status=True),
        'questions': FrequentlyQuestions.objects.filter(status=True)[::-1],
        }
    
    return render(request, 'root/index.html', context=context)


def contact(request):
    return render(request, "root/contact.html")


def about(request):
    return render(request, "root/about.html")

# Create your views here.
