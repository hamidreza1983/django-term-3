from celery import shared_task
from mail_templated import send_mail
from accounts.models import CustomUser, Advertisement

@shared_task
def send_email(template_name:str, redirect_link:dict, from_user:str, to_users:list):
    send_mail(
            template_name,
            redirect_link,
            from_user,
            to_users,
        )
    
# @shared_task
# def clean_user():
#     unverified_users = CustomUser.objects.filter(is_verified=False)
#     unverified_users.delete()
#     print ("unverified_users deleted ... ")


# @shared_task
# def send_adv(number, name=None):
#     adv = Advertisement.objects.get(id=1)
#     all_users = CustomUser.objects.all()
#     email_list = [user.email for user in all_users]
#     send_mail(
#         "email/adv.html",
#         {"text" : adv.text},
#         "admin@admin.com",
#         email_list 
#     )
