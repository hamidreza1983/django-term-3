from rest_framework.generics import GenericAPIView
from .serializer import RegistrationSerializer, CustomAuthTokenSerializer, CustomTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from threading import Thread
import time
from rest_framework_simplejwt.views import  TokenObtainPairView



class RegistrationView(GenericAPIView):
    serializer_class = RegistrationSerializer

    
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'email' : serializer.validated_data['email'],
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class CustomObtainAuthToken(ObtainAuthToken):

    serializer_class = CustomAuthTokenSerializer

    # def delete_token(self, request, *args, **kwargs):
    #     time.sleep(300)

    #     request.user.auth_token.delete()

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        # tr1 = Thread(target=self.delete_token)
        # tr1.start()
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'is_superuser':user.is_superuser
        })
        
class DeleteTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer