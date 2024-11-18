from celery import shared_task
from mail_templated import send_mail

@shared_task
def send_email(template_name:str, redirect_link:dict, from_user:str, to_users:list):
    send_mail(
            template_name,
            redirect_link,
            from_user,
            to_users,
        )