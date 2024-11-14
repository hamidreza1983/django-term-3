from rest_framework.generics import GenericAPIView
from .serializer import (
    RegistrationSerializer,
    CustomAuthTokenSerializer,
    CustomTokenObtainPairSerializer,
    ChangePasswordSerializer,
    ResendEmailSerializer,
)
from .serializer import (
    ResendEmailSerializer,
    RegistrationSerializer,
    CustomAuthTokenSerializer,
    CustomTokenObtainPairSerializer,
    ChangePasswordSerializer,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.mail import send_mail
from ...models import CustomUser
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken
from threading import Thread
import time
from mail_templated import send_mail
from accounts.api.v1.tasks import test


class RegistrationView(GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data["email"]
            user = get_object_or_404(CustomUser, email=email)
            if not user.is_verified:
                send_mail(
                    "verify",
                    f"http://127.0.0.1:8000/accounts/api/v1/verify-mail/{self.get_tokens_for_user(user)}",
                    "admin@admin.com",
                    [email],
                )
                return Response(
                    {
                        "email message send for you",
                    }
                )
            else:
                return Response(
                    {
                        "okeye",
                    }
                )

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return str(refresh.access_token)


class CustomObtainAuthToken(ObtainAuthToken):

    serializer_class = CustomAuthTokenSerializer

    # def delete_token(self, request, *args, **kwargs):
    #     time.sleep(300)

    #     request.user.auth_token.delete()

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        # tr1 = Thread(target=self.delete_token)
        # tr1.start()
        return Response(
            {
                "token": token.key,
                "user_id": user.pk,
                "email": user.email,
                "is_superuser": user.is_superuser,
            }
        )


class DeleteTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ChangePasswordView(GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.old_password_check(serializer.validated_data, request)
        serializer.new_password_set(serializer.validated_data, request)
        token = serializer.delete_old_token_and_create_new(
            serializer.validated_data, request
        )
        return Response(
            {
                "detail": f"password reset successfully and your new token is {token.key}"
            },
            status=status.HTTP_200_OK,
        )


class VerifyEmailView(APIView):

    def get(self, request, *args, **kwargs):
        token = kwargs.get("token")
        data = AccessToken(token)
        user_id = data["user_id"]
        user = get_object_or_404(CustomUser, id=user_id)
        user.is_verified = True
        user.save()
        return Response({"detail : your account has been verified"})


class ResendVerifyEmailView(GenericAPIView):
    serializer_class = ResendEmailSerializer

    # def send_mail_with_thread(self, subject:str, url:str, src:str, dest:list):
    #                             time.sleep(5)
    #                             send_mail(
    #                                         subject,
    #                                         url,
    #                                         src,
    #                                         dest,
    #                                     )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            if not user.is_verified:
                token = self.get_tokens_for_user(user)
                send_mail(
                    "email/email-temp.html",
                    {"token": token},
                    "admin@admin.com",
                    [user.email],
                )

                # subject = "please verify your email"
                # url = f"http://127.0.0.1:8000/accounts/api/v1/verify-mail/{self.get_tokens_for_user(user)}"
                # src = "admin@admin.com"
                # dest = [user.email]
                # tr = Thread(target=self.send_mail_with_thread, args=(subject, url, src, dest))
                # tr.start()
                return Response(
                    {
                        "email message Resend for you",
                    }
                )
            else:
                return Response(
                    {
                        "your email is already verified",
                    }
                )

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
