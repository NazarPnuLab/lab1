from django.core.mail import EmailMessage
from django.conf import settings


def send_email(subject, message, recipients):
    try:
        email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, recipients)
        email.send()
    except Exception as e:
        print(f"Error sending email: {e}")




