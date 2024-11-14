from celery import shared_task
from mail_templated import send_mail


@shared_task
def test():
    print ("mail send succefully")
    return "mail send succefully"