from django.contrib import admin
from .models import CustomUser, Profile

admin.site.register(CustomUser)
admin.site.register(Profile)

# Register your models here.
