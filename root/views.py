from django.shortcuts import render
from services.models import SpecialService
from .models import FrequentlyQuestions
from services.models import Team


from django.http import HttpResponse


def home(request):

    context = {
        'specials': SpecialService.objects.filter(status=True),
        'team' : Team.objects.filter(status=True),
        'questions': FrequentlyQuestions.objects.filter(status=True)[::-1],
        }
    
    return render(request, 'root/index.html', context=context)


def contact(request):
    return render(request, "root/contact.html")


def about(request):
    context = {
        'team' : Team.objects.filter(status=True),
        }
    return render(request, "root/about.html", context=context)

# Create your views here.
