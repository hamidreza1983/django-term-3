from django.http import HttpResponse

from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

app_name = 'root'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contactus/', contact, name='contact'),
    path('about/', cache_page(60)(AboutView.as_view()), name='about'),
]
