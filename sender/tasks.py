# -*- coding: utf-8 -*-

from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, get_connection

from accounts.models import OwnerRespondent
from config.settings import EMAIL_HOST_USER, DEFAULT_DOMAIN
from sender.models import Mailing


@shared_task
def send_mailing(parameters):
    send_data = []
    user_from = User.objects.get(pk=parameters.get('owner'))
    users_to = OwnerRespondent.objects.filter(owner=user_from)
    mailing = Mailing.objects.get(pk=parameters.get('mailing'))
    for recipient in users_to:
        html_msg = mailing.body.replace(
            '{user}', recipient.subscriber.first_name
        ).replace(
            '{owner}', user_from.first_name
        )
        # .replace('src="/', 'src="{}'.format(DEFAULT_DOMAIN))

        single_data = EmailMultiAlternatives(
            mailing.title,
            html_msg,
            EMAIL_HOST_USER,
            [recipient.subscriber.email, ]
        )
        single_data.attach_alternative(html_msg, 'text/html')
        send_data.append(single_data)
    print send_data
    connection = get_connection()
    connection.send_messages(send_data)
