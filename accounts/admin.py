from django.contrib import admin
from .models import CustomUser, Profile
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'is_staff']
    list_filter = ['is_verified', 'is_superuser']
    search_fields = ['email']
    ordering = ['email']
    fieldsets = (
        (
            "Info", {
                "fields" : ('email', "password")
            }
        ),
        (
            "Permissions",  {
                "classes" : ("collapse", ),
                "fields" : ("is_staff", "is_active", "is_verified", "is_superuser", "groups", "user_permissions")
            }

        ),
    )
    add_fieldsets = (
        (
            "Info", {
                "fields" : ('email', "password1", "password2")
            }
        ),
        # (
        #     "Permissions",  {
        #         "classes" : ("collapse", ),
        #         "fields" : ("is_staff", "is_active", "is_verified", "is_superuser", "groups", "user_permissions")
        #     }

        # ),
    )




admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)

