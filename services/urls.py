from django.urls import path, include
from .views import *
from django.views.generic import RedirectView


app_name = 'services'

urlpatterns = [
    path('', ServiceView.as_view(), name='services'),
    path('category/<str:category>', ServiceView.as_view(), name='list_by_category'),
    path('price/<int:price>', ServiceView.as_view(), name='list_by_price'),
    #path('service-detail/<int:pk>', services_detail, name='services-detail'),
    path('service-detail/<int:pk>', ServiceDetaiView.as_view(), name='services-detail'),
    path('qoute/', qoute, name='qoute'),
    path("comment/edit/<int:id>", edit_comment, name='edit_comment'),
    path("adv", GoogleView.as_view(), name='adv1'),
    path("api/v1/",include("services.api.v1.urls")),
]