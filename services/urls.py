from django.urls import path
from .views import *


app_name = 'services'

urlpatterns = [
    path('', ServiceView.as_view(), name='services'),
    path('category/<str:category>', ServiceView.as_view(), name='list_by_category'),
    path('price/<int:price>', ServiceView.as_view(), name='list_by_price'),
    path('service-detail/<int:id>', services_detail, name='services-detail'),
    path('qoute/', qoute, name='qoute'),
    path("comment/edit/<int:id>", edit_comment, name='edit_comment'),
]
