# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import CustomUser, Profile

# @receiver(post_save, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         print (instance.email)
#         Profile.objects.create(user=instance)


