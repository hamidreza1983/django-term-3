from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomeUser(AbstractUser):
    id_code = models.CharField(max_length=10, unique=True)
    phone = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to='user', default='default.jpg')

    def __str__(self):
        return self.username
