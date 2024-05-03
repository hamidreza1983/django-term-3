from django.http import HttpResponse

from django.urls import path
from .views import *

app_name = 'root'

urlpatterns = [
    path('', home, name='home'),
    path('contactus/', contact, name='contact'),
    path('about/', about, name='about'),
]
