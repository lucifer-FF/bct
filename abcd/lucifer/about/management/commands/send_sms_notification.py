"""
Django management command to send SMS notifications to customers

Usage:
    python manage.py send_sms_notification --order-id=1 --type=confirmation
    python manage.py send_sms_notification --phone="+1234567890" --message="Your message here"
"""

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from about.models import Order
from about.sms_service import (
    send_order_confirmation_sms,
    send_order_shipped_sms,
    send_order_delivered_sms,
    send_custom_sms
)


class Command(BaseCommand):
    help = 'Send SMS notifications to customers'

    def add_arguments(self, parser):
        parser.add_argument(
            '--order-id',
            type=int,
            help='Order ID to send notification for',
        )
        parser.add_argument(
            '--type',
            type=str,
            choices=['confirmation', 'shipped', 'delivered'],
            default='confirmation',
            help='Type of order notification',
        )
        parser.add_argument(
            '--phone',
            type=str,
            help='Phone number to send custom SMS to',
        )
        parser.add_argument(
            '--message',
            type=str,
            help='Custom message to send',
        )

    def handle(self, *args, **options):
        if not settings.SMS_ENABLED:
            self.stdout.write(
                self.style.ERROR(
                    'SMS is not configured. Please set Twilio credentials in environment variables.'
                )
            )
            return

        # Custom SMS
        if options['phone'] and options['message']:
            self.stdout.write('Sending custom SMS...')
            success = send_custom_sms(options['phone'], options['message'])
            if success:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'SMS sent successfully to {options["phone"]}'
                    )
                )
            else:
                self.stdout.write(
                    self.style.ERROR(
                        f'Failed to send SMS to {options["phone"]}'
                    )
                )
            return

        # Order notification
        if not options['order_id']:
            raise CommandError('Please provide either --order-id or --phone and --message')

        try:
            order = Order.objects.get(id=options['order_id'])
        except Order.DoesNotExist:
            raise CommandError(f'Order with ID {options["order_id"]} does not exist')

        notification_type = options['type']
        self.stdout.write(f'Sending {notification_type} SMS for order {order.order_number}...')

        if notification_type == 'confirmation':
            success = send_order_confirmation_sms(order)
        elif notification_type == 'shipped':
            success = send_order_shipped_sms(order)
        elif notification_type == 'delivered':
            success = send_order_delivered_sms(order)

        if success:
            self.stdout.write(
                self.style.SUCCESS(
                    f'{notification_type.capitalize()} SMS sent to {order.phone}'
                )
            )
        else:
            self.stdout.write(
                self.style.ERROR(
                    f'Failed to send {notification_type} SMS'
                )
            )
