from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser,  BaseUserManager, PermissionsMixin
from django.utils import timezone


# class CustomeUser(AbstractUser):
#      id_code = models.CharField(max_length=10, blank=True, null=True)
#      phone = models.CharField(max_length=11, blank=True, null=True)
#      address = models.CharField(max_length=250, null=True, blank=True)
#      image = models.ImageField(upload_to='user', default='default.jpg')
#      def __str__(self):
#          return self.username
    
class CustomeBaseUserManager(BaseUserManager):
    def create_user(self,email, password, **extra_fields):
        if not email:
            raise ValueError('email can not be empty')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_verified', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('super user can not be create  .. is_staff cant be false')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('super user can not be create  .. is_superuser cant be false')
        if extra_fields.get('is_verified') is not True:
            raise ValueError('super user can not be create  .. is_verified cant be false')
        # if extra_fields.get('is_active') is not True:
        #     raise ValueError('super user can not be create  .. is_active cant be false')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
   email = models.EmailField(unique=True)
   is_active = models.BooleanField(default=True)
   is_staff = models.BooleanField(default=False)
   is_superuser = models.BooleanField(default=False)
   is_verified = models.BooleanField(default=False)
   created_at = models.DateTimeField(default=timezone.now)
   updated_at = models.DateTimeField(default=timezone.now)
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = []
   objects = CustomeBaseUserManager()

   def __str__(self):
       return self.email
   

class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='profile', default='default.jpg')

    def __str__(self):
        return self.user.email

