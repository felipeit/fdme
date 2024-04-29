from .celery import app
from django.core.mail import send_mail



@app.task
def send_email_task(subject, message, from_email, recipient_list) -> None:
    send_mail(subject, message, from_email, recipient_list)
