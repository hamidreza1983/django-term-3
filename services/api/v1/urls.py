from django.urls import path
from .views import *

app_name = "services-api"

urlpatterns = [
    path("services", services, name="services")
]
