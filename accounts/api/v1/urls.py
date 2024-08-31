from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

app_name = "account-api"

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    #path('token/login', CustomObtainAuthToken.as_view(), name="login"),
    path('token/logout', DeleteTokenView.as_view(), name="logout"),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
]