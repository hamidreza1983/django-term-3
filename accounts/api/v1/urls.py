from django.urls import path
from .views import *
app_name = "account-api"

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('token/login', CustomObtainAuthToken.as_view(), name="login"),
]