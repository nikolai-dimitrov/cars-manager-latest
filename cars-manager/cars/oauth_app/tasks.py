from celery import shared_task

from cars.core.emails import send_delete_code_to_email


@shared_task
def send_mail_async(email, delete_code):
    send_delete_code_to_email(email, delete_code)
