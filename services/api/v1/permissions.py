from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.method == "GET" or (request.user.is_authenticated and request.user.is_superuser))
    

    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        else:
            return bool(request.user.is_authenticated and request.user.is_superuser)