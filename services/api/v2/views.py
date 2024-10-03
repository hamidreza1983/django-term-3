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
    

