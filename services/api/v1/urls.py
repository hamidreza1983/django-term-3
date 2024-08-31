from django.urls import path
from .views import *

app_name = "services-api"

urlpatterns = [
    path("services", ServicesApiViewSet.as_view({'get' : 'list', 'post': 'create'}), name="services"),
    path("services/<int:pk>", ServicesApiViewSet.as_view({'get' : 'retrieve', 'patch' : 'update', 'delete' : 'destroy'}), name="services_detail"),
    path("team", TeamApiViewSet.as_view({'get' : 'list', 'post': 'create'}), name="teams"),
    path("team/<int:pk>", TeamApiViewSet.as_view({'get' : 'retrieve', 'patch' : 'update', 'delete' : 'destroy'}), name="team_detail"),
    path("comments", CommentApiViewSet.as_view({'get' : 'list', 'post': 'create'}), name="teams"),
    path("comments/<int:pk>", CommentApiViewSet.as_view({'get' : 'retrieve', 'patch' : 'update', 'delete' : 'destroy'}), name="team_detail"),
]


# urlpatterns = [
#     path("services", ServicesApiViewSet.as_view(), name="services"),
#     path("services/<int:pk>", ServicesApiViewSet.as_view(), name="services_detail")
# ]
