from django.shortcuts import render
from services.models import SpecialService


from django.http import HttpResponse


def home(request):
    return render(request, 'root/index.html', context={'specials': SpecialService.objects.all()})


def contact(request):
    return render(request, "root/contact.html")


def about(request):
    return render(request, "root/about.html")

# Create your views here.
