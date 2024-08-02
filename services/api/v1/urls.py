from django.urls import path
from .views import *

app_name = "services-api"

urlpatterns = [
    path("services", services, name="services"),
    path("services/<int:id>", services_detail, name="services_detail")
]
