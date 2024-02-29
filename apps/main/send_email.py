
from celery import shared_task
from config.celery import app
import datetime

from django.core.mail import send_mail
import os


@app.task(max_retries=1)
def send_email(recipient_list, *args, **kwargs):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = os.getenv('EMAIL_HOST_USER')
    send_mail(subject, message, email_from, recipient_list)
    return 'send mail success'


@shared_task
def send_email_date(*args, **kwargs):
    time = datetime.datetime.now().strftime('%d %m %Y %H:%M%S')
    subject = 'Thank you for registering to our'
    message = f'{time} is now'
    email_from = os.getenv('EMAIL_HOST_USER')
    send_mail(subject, message, email_from, ['ozodjonsalohiddinov08@gmail.com', 'mirzonafasov20@gmail.com', ])
    return 'send mail success time'
