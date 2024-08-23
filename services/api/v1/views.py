from rest_framework.response import Response
from services.models import Services, Team, Comments
from .serializer import ServiceSerializer, TeamSerializer, CommentsSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.exceptions import MethodNotAllowed
from .paginate import Custompagination



class ServicesApiViewSet(viewsets.ModelViewSet):
       
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'name']
    search_fields = ['price']
    ordering_fields = ['created_at']
    pagination_class = Custompagination


    def get_queryset(self):
       return Services.objects.all()
    

class TeamApiViewSet(viewsets.ModelViewSet):
    
    serializer_class = TeamSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
       return Team.objects.all()
    

class CommentApiViewSet(viewsets.ModelViewSet):
    
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
       return Comments.objects.all()

    def destroy(self, request, *args, **kwargs):
        comment = get_object_or_404(Comments, id=kwargs.get('pk'))
        if comment.user == request.user:
            comment.delete()
            return Response("service deleted successfully", status=status.HTTP_204_NO_CONTENT)
        else:
            raise MethodNotAllowed("DELETE")





# class ServicesApiViewSet(viewsets.ViewSet):

#    serializer_class = ServiceSerializer

#    def get_queryset(self):
#       return Services.objects.all()
   
#    def list(self, request, *args, **kwargs):
#       serializer =self.serializer_class(self.get_queryset(), many=True)
#       return Response(serializer.data)
   
#    def create (self, request, *args, **kwargs):
#       serializer =self.serializer_class(data=request.data)
#       if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#       else:
#             return Response(serializer.error)
      
#    def update (self, request, *args, **kwargs):
#          services = get_object_or_404(Services, id=kwargs.get('pk'))
#          serializer =self.serializer_class(services, data=request.data)
#          serializer.is_valid(raise_exception=True)
#          serializer.save()
#          return Response(serializer.data, status=status.HTTP_200_OK)

#    def destroy(self, request, *args, **kwargs):
#       services = get_object_or_404(Services, id=kwargs.get('pk'))
#       services.delete()
#       return Response("service deleted successfully", status=status.HTTP_204_NO_CONTENT)
      
#    def retrieve(self, request, *args, **kwargs):
#       services = get_object_or_404(Services, id=kwargs.get('pk'))
#       serializer =self.serializer_class(services)
#       return Response(serializer.data, status=status.HTTP_200_OK)
   






# class ServicesApiView(GenericAPIView, ListModelMixin, CreateModelMixin):
#    permission_classes = [IsAuthenticatedOrReadOnly]
#    serializer_class = ServiceSerializer

#    def get_queryset(self):
#       return Services.objects.all()
   
#    def get(self, request, *args, **kwargs):
#       return self.list(request, *args, **kwargs)

#    def post(self, request, *args, **kwargs):
#       return self.create(request, *args, **kwargs)



# class ServiceDetailApiView(GenericAPIView, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin):
      
#       permission_classes = [IsAuthenticatedOrReadOnly]
#       serializer_class = ServiceSerializer
#       lookup_field = 'id'

#       def get_queryset(self):
#          return Services.objects.all()

#       def get(self, request, *args, **kwargs):
#          return self.retrieve(request, *args, **kwargs)
      
#       def patch (self, request, *args, **kwargs):
#          return self.update(request, *args, **kwargs)

#       def delete (self, request, *args, **kwargs):
#          return self.destroy(request, *args, **kwargs)
      


# class ServicesApiView(APIView):
#    permission_classes = [IsAuthenticatedOrReadOnly]

#    def get(self, request, *args, **kwargs):
#       services = Services.objects.all()
#       serializer =ServiceSerializer(services, many=True)
#       return Response(serializer.data)

#    def post(self, request, *args, **kwargs):
#       if request.user.is_superuser:
#          serializer =ServiceSerializer(data=request.data)
#          if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#          else:
#             return Response(serializer.error)
#       else:
#           return Response("permission denied", status=status.HTTP_401_UNAUTHORIZED)

# class ServiceDetailApiView(APIView):
#       permission_classes = [IsAuthenticatedOrReadOnly]
      

#       def get(self, request, *args, **kwargs):
#          id = kwargs.get('id')
#          services = get_object_or_404(Services, id=id)
#          serializer =ServiceSerializer(services)
#          return Response(serializer.data)
      
#       def patch (self, request, *args, **kwargs):
#          services = get_object_or_404(Services, id=id)
#          serializer =ServiceSerializer(services, data=request.data)
#          serializer.is_valid(raise_exception=True)
#          serializer.save()
#          return Response(serializer.data, status=status.HTTP_200_OK)

#       def delete (self, request, *args, **kwargs):
#          services = get_object_or_404(Services, id=id)
#          services.delete()
#          return Response("service deleted successfully", status=status.HTTP_204_NO_CONTENT)


# @api_view(["GET", "POST"])
# #@permission_classes([IsAuthenticatedOrReadOnly])
# def services(request):
#    if request.method == "GET":
#       services = Services.objects.all()
#       serializer =ServiceSerializer(services, many=True)
#       return Response(serializer.data)
#    elif request.method == "POST":
#       if request.user.is_superuser:
#          serializer =ServiceSerializer(data=request.data)
#          if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#          else:
#             return Response(serializer.error)
#       else:
#          return Response("permission denied", status=status.HTTP_401_UNAUTHORIZED)
      

# @api_view(["GET", "PATCH", "DELETE"])

# def services_detail(request, id):
#    service = get_object_or_404(Services, id=id)
#    if request.method == "GET":
#       # try:
#       #    services = Services.objects.get(id=id)
#       #    serializer =ServiceSerializer(services)
#       #    return Response(serializer.data)
#       # except:
#       #    return Response("object does not exist", status=status.HTTP_404_NOT_FOUND)
      
#       serializer =ServiceSerializer(service)
#       return Response(serializer.data)
#    elif request.method == "PATCH":
#       serializer =ServiceSerializer(service, data=request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_200_OK)
   
#    elif request.method == "DELETE":
#       service.delete()
#       return Response("service deleted successfully", status=status.HTTP_204_NO_CONTENT)


