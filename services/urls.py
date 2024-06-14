from django.urls import path
from .views import *


app_name = 'services'

urlpatterns = [
    path('', services, name='services'),
    path('category/<str:category>', services, name='list_by_category'),
    path('price/<int:price>', services, name='list_by_price'),
    path('service-detail/<int:id>', services_detail, name='services-detail'),
    path('qoute/', qoute, name='qoute'),
    path("comment/edit/<int:id>", edit_comment, name='edit_comment'),
]
