
from celery import shared_task
from config.celery import app

from django.core.mail import send_mail
import os


@app.task(max_retries=1)
def send_email(recipient_list, *args, **kwargs):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = os.getenv('EMAIL_HOST_USER')
    send_mail(subject, message, email_from, recipient_list)
