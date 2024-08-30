from rest_framework import serializers
from ...models import CustomUser
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.authtoken.models import Token


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        validate_data = super().validate(attrs)
        validate_data['user'] = self.user.id
        validate_data['email'] = self.user.email

        return validate_data
        

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



class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=("email"),
        write_only=True
    )
    password = serializers.CharField(
        label=("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=("Token"),
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('email')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = ('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = ('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
    

class ChangePasswordSerializer(serializers.Serializer):

    old_pass = serializers.CharField(max_length=30)
    new_pass1 = serializers.CharField(max_length=30)
    new_pass2 = serializers.CharField(max_length=30)

    def validate(self, attrs):
        pass1 = attrs.get("new_pass1")
        pass2 = attrs.get("new_pass2")

        if pass1 != pass2:
            msg = ('pass1 and pass2 must be the same')
            raise serializers.ValidationError(msg, code='authorization')

        return super().validate(attrs)
    

    def old_password_check(self, attrs, request):
        old_pass = attrs.get("old_pass")
        user = request.user

        if not user.check_password(old_pass):
            msg = ('Old pass doesnt match')
            raise serializers.ValidationError(msg, code='authorization')
        return attrs
    
    def new_password_set(self, attrs, request):
        pass1 = attrs.get("new_pass1")
        user = request.user
        try:
            validate_password(pass1)

        except:
            raise serializers.ValidationError ({
                'detail' : "validate password fail..."
            })
        
        user.set_password(pass1)
        return attrs
    
    def delete_old_token_and_create_new(self, attrs, request):
        user = request.user
        user.auth_token.delete()
        token = Token.objects.create(user=user)
        return token

