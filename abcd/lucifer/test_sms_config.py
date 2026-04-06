#!/usr/bin/env python
import os
import sys
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lucifer.settings')
django.setup()

from django.conf import settings
print("\n" + "="*60)
print("SMS CONFIGURATION VERIFICATION")
print("="*60)

# Check environment variables
print("\n✓ Environment Variables:")
print(f"  TWILIO_ACCOUNT_SID: {settings.TWILIO_ACCOUNT_SID[:15]}...")
print(f"  TWILIO_AUTH_TOKEN: {settings.TWILIO_AUTH_TOKEN[:15]}...")
print(f"  TWILIO_PHONE_NUMBER: {settings.TWILIO_PHONE_NUMBER}")

# Check SMS enabled status
print(f"\n✓ SMS System Status:")
print(f"  SMS_ENABLED: {settings.SMS_ENABLED}")

if not settings.SMS_ENABLED:
    print("\n✗ ERROR: SMS is disabled!")
    print("  Check your environment variables are set correctly.")
    sys.exit(1)

# Test Twilio client
print(f"\n✓ Testing Twilio Client:")
try:
    from twilio.rest import Client
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    account = client.api.accounts(settings.TWILIO_ACCOUNT_SID).fetch()
    print(f"  Account Status: {account.status}")
    print(f"  Account Type: {account.type}")
    print(f"  ✓ Twilio connection successful!")
except Exception as e:
    print(f"  ✗ Twilio error: {e}")
    sys.exit(1)

# Test SMS service import
print(f"\n✓ SMS Service Import:")
try:
    from about.sms_service import send_custom_sms, send_order_confirmation_sms
    print(f"  ✓ SMS service functions imported successfully")
except Exception as e:
    print(f"  ✗ Import error: {e}")
    sys.exit(1)

# Test database model
print(f"\n✓ Database Model:")
try:
    from about.models import SMSNotification, Order
    sms_count = SMSNotification.objects.count()
    print(f"  Total SMS in database: {sms_count}")
    print(f"  ✓ SMS model accessible")
except Exception as e:
    print(f"  ✗ Model error: {e}")
    sys.exit(1)

print("\n" + "="*60)
print("✓ SMS SYSTEM IS FULLY CONFIGURED AND READY!")
print("="*60)
print("\nNext Steps:")
print("1. Test SMS with: python manage.py send_sms_notification --phone=+917001945496 --message='Test'")
print("2. Run server: python manage.py runserver")
print("3. Place a test order to verify automatic SMS")
print()
