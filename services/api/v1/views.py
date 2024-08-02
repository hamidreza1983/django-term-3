from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from services.models import Services
from .serializer import ServiceSerializer, ServiceDetailSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def services(request):
   if request.method == "GET":
      services = Services.objects.all()
      serializer =ServiceSerializer(services, many=True)
      return Response(serializer.data)
   elif request.method == "POST":
      if request.user.is_superuser:
         serializer =ServiceSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         else:
            return Response(serializer.error)
      else:
         return Response("permission denied", status=status.HTTP_401_UNAUTHORIZED)
      

@api_view(["GET", "PATCH", "DELETE"])

def services_detail(request, id):
   service = get_object_or_404(Services, id=id)
   if request.method == "GET":
      # try:
      #    services = Services.objects.get(id=id)
      #    serializer =ServiceSerializer(services)
      #    return Response(serializer.data)
      # except:
      #    return Response("object does not exist", status=status.HTTP_404_NOT_FOUND)
      
      serializer =ServiceSerializer(service)
      return Response(serializer.data)
   elif request.method == "PATCH":
      serializer =ServiceSerializer(service, data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
   
   elif request.method == "DELETE":
      service.delete()
      return Response("service deleted successfully", status=status.HTTP_204_NO_CONTENT)


