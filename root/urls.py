from django.http import HttpResponse

from django.urls import path
from .views import *

app_name = 'root'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contactus/', contact, name='contact'),
    path('about/', AboutView.as_view(), name='about'),
]
