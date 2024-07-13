from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser,  BaseUserManager, PermissionsMixin


class CustomeUser(AbstractUser):
     id_code = models.CharField(max_length=10, blank=True, null=True)
     phone = models.CharField(max_length=11, blank=True, null=True)
     address = models.CharField(max_length=250, null=True, blank=True)
     image = models.ImageField(upload_to='user', default='default.jpg')
     def __str__(self):
         return self.username
    

#class CustomUser(AbstractBaseUser, PermissionsMixin):
#    email = models.EmailField(unique=True)
#    is_active = models.BooleanField(default=True)
#    is_staff = models.BooleanField(default=False)
#    is_superuser = models.BooleanField(default=False)
#    is_verfied = models.BooleanField(default=False)


