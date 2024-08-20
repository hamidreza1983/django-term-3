from rest_framework import serializers
from ...models import CustomUser
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError

class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=100)
    
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'password1']


    def validate(self, attrs):
        pass1 = attrs["password"]
        pass2 = attrs["password1"]

        if pass1 != pass2:
            
            raise serializers.ValidationError({
                'detail' : 'you are very donkey'
            })
        
        try:

            validate_password(pass1)
        except ValidationError as e:
            raise serializers.ValidationError ({
                'detail' : list(e.messages)
            })
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('password1')
        return CustomUser.objects.create_user(**validated_data)