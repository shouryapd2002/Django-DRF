import logging
from django.core.mail import send_mail
from celery import shared_task
from .models import EmailStatus
from .utils import parse_recipients

logger = logging.getLogger(__name__)

@shared_task(rate_limit='100/m')
def send_bulk_emails(subject, body, recipients, attachment=None):
    recipient_list = parse_recipients(recipients)
    for recipient in recipient_list:
        try:
            personalized_body = body.replace('{{name}}', recipient['name'])
            send_mail(
                subject,
                personalized_body,
                'trydjango.email.host@gmail.com',
                [recipient['email']],
                fail_silently=False,
            )
            EmailStatus.objects.create(recipient=recipient['email'], status='sent')

        except Exception as e:
            logger.error(f"Failed to send email to {recipient['email']}: {str(e)}")
            EmailStatus.objects.create(recipient=recipient['email'], status=f'failed: {str(e)}')