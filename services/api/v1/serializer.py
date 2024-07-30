from rest_framework import serializers
from services.models import Services


# class ServiceSerializer(serializers.Serializer):

#     name = serializers.CharField(max_length=100)
#     image = serializers.ImageField()
#     title = serializers.CharField(max_length=100)
#     content = serializers.CharField(max_length=100)


class ServiceSerializer(serializers.ModelSerializer):
    
    class Meta : 
        model = Services
        fields = "__all__"