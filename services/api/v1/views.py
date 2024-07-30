from rest_framework.decorators import api_view
from rest_framework.response import Response
from services.models import Services
from .serializer import ServiceSerializer


@api_view()
def services(request):
   services = Services.objects.all()
   serializer =ServiceSerializer(services, many=True)
   return Response(serializer.data)