from rest_framework.generics import GenericAPIView
from .serializer import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status




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
