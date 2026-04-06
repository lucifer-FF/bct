"""
SMS Service for sending order confirmations and other notifications
Uses Twilio API for SMS delivery
"""

from django.conf import settings
from twilio.rest import Client
import logging

logger = logging.getLogger(__name__)


def _log_sms_notification(order, phone_number, message_body, notification_type, status, twilio_sid=None):
    """Log SMS notification to database"""
    try:
        from .models import SMSNotification
        SMSNotification.objects.create(
            order=order,
            phone_number=phone_number,
            message=message_body,
            notification_type=notification_type,
            status=status,
            twilio_sid=twilio_sid
        )
    except Exception as e:
        logger.error("Failed to log SMS notification: %s", str(e))


def send_order_confirmation_sms(order):
    """
    Send order confirmation SMS to customer
    
    Args:
        order: Order instance
    """
    
    # Check if SMS is enabled
    if not settings.SMS_ENABLED:
        logger.info("SMS is not enabled. Skipping SMS notification for order %s", order.order_number)
        _log_sms_notification(order, order.phone, "", "confirmation", "failed")
        return False
    
    try:
        # Initialize Twilio client
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        
        # Format order items list
        items_text = ", ".join([
            f"{item.quantity}x {item.product.name}"
            for item in order.items.all()
        ])
        
        # Create SMS message
        message_body = f"""
Order Confirmation ✓

Order #: {order.order_number}
Items: {items_text}
Total: ${order.total_amount}
Status: {order.get_status_display()}

Your order will be shipped to:
{order.address}
{order.city}, {order.state} {order.zipcode}

Thank you for your purchase!
        """.strip()
        
        # Send SMS
        message = client.messages.create(
            body=message_body,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=order.phone  # Customer phone number
        )
        
        logger.info("SMS sent successfully for order %s. SID: %s", order.order_number, message.sid)
        _log_sms_notification(order, order.phone, message_body, "confirmation", "sent", message.sid)
        return True
        
    except Exception as e:
        logger.error("Failed to send SMS for order %s: %s", order.order_number, str(e))
        _log_sms_notification(order, order.phone, "", "confirmation", "failed")
        return False


def send_order_shipped_sms(order):
    """
    Send order shipped notification SMS
    
    Args:
        order: Order instance
    """
    
    if not settings.SMS_ENABLED:
        logger.info("SMS is not enabled. Skipping SMS notification for order %s", order.order_number)
        _log_sms_notification(order, order.phone, "", "shipped", "failed")
        return False
    
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        
        message_body = f"""
Your order has been shipped! 📦

Order #: {order.order_number}
Estimated Delivery: 3-5 business days
Total: ${order.total_amount}

Track your order and manage preferences in your account.

Thank you!
        """.strip()
        
        message = client.messages.create(
            body=message_body,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=order.phone
        )
        
        logger.info("Shipped SMS sent for order %s. SID: %s", order.order_number, message.sid)
        _log_sms_notification(order, order.phone, message_body, "shipped", "sent", message.sid)
        return True
        
    except Exception as e:
        logger.error("Failed to send shipped SMS for order %s: %s", order.order_number, str(e))
        _log_sms_notification(order, order.phone, "", "shipped", "failed")
        return False


def send_order_delivered_sms(order):
    """
    Send order delivered notification SMS
    
    Args:
        order: Order instance
    """
    
    if not settings.SMS_ENABLED:
        logger.info("SMS is not enabled. Skipping SMS notification for order %s", order.order_number)
        _log_sms_notification(order, order.phone, "", "delivered", "failed")
        return False
    
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        
        message_body = f"""
Your order has been delivered! ✓

Order #: {order.order_number}
Total: ${order.total_amount}

We'd love to hear from you! Please leave a review.

Thank you for shopping with us!
        """.strip()
        
        message = client.messages.create(
            body=message_body,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=order.phone
        )
        
        logger.info("Delivered SMS sent for order %s. SID: %s", order.order_number, message.sid)
        _log_sms_notification(order, order.phone, message_body, "delivered", "sent", message.sid)
        return True
        
    except Exception as e:
        logger.error("Failed to send delivered SMS for order %s: %s", order.order_number, str(e))
        _log_sms_notification(order, order.phone, "", "delivered", "failed")
        return False


def send_custom_sms(phone_number, message_text):
    """
    Send custom SMS to a phone number
    
    Args:
        phone_number: Customer phone number (with country code)
        message_text: Message to send
        
    Returns:
        bool: True if sent successfully, False otherwise
    """
    
    if not settings.SMS_ENABLED:
        logger.info("SMS is not enabled. Skipping custom SMS")
        return False
    
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        
        message = client.messages.create(
            body=message_text,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        
        logger.info("Custom SMS sent to %s. SID: %s", phone_number, message.sid)
        _log_sms_notification(None, phone_number, message_text, "custom", "sent", message.sid)
        return True
        
    except Exception as e:
        logger.error("Failed to send custom SMS to %s: %s", phone_number, str(e))
        _log_sms_notification(None, phone_number, message_text, "custom", "failed")
        return False
