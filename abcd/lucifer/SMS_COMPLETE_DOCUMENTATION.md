# SMS Notification System - Complete Documentation

## Overview
Your Django ecommerce platform now includes a complete SMS notification system using **Twilio**. Customers automatically receive SMS confirmations when they place orders, and admins can send additional notifications.

## What's Included

### 1. **Automatic Order Confirmation SMS** ✅
- Triggered immediately after order placement
- Includes order number, items, total price, and shipping address
- Sent to customer's phone number from checkout form

### 2. **SMS Notification Tracking** ✅
- New `SMSNotification` model to log all SMS messages
- Track delivery status in Django Admin
- Store Twilio message SID for reference
- View notification history per order

### 3. **Additional SMS Types** ✅
- **Order Shipped**: Manual notification for when orders ship
- **Order Delivered**: Manual notification for when orders arrive
- **Custom SMS**: Send promotional or custom messages to customers

### 4. **Management Command** ✅
Send SMS from command line or scripts:
```bash
python manage.py send_sms_notification --order-id=1 --type=confirmation
python manage.py send_sms_notification --phone="+1234567890" --message="Custom message"
```

### 5. **Admin Interface** ✅
- View all SMS messages sent to customers
- Filter by status (sent/failed)
- See notification type and timestamp
- View associated orders

## Architecture

### Models

#### SMSNotification (New)
```python
- order: Foreign Key to Order
- phone_number: Customer phone
- message: SMS text
- notification_type: confirmation, shipped, delivered, custom
- status: sent, failed, pending
- twilio_sid: Twilio message ID
- created_at: Timestamp
```

#### Order (Updated)
- Already has `phone` field for SMS delivery

### Views (Updated)

#### checkout()
- Imports `send_order_confirmation_sms`
- Calls SMS service after order creation
- Shows status message to customer

### Services

#### sms_service.py (New)
Functions:
- `send_order_confirmation_sms(order)` - Auto confirmation
- `send_order_shipped_sms(order)` - Manual shipped
- `send_order_delivered_sms(order)` - Manual delivered
- `send_custom_sms(phone, message)` - Custom messages
- `_log_sms_notification()` - Internal logging

### Admin

#### SMSNotificationAdmin (New)
- List display: phone, type, status, created_at
- Search: phone, order number
- Filter: status, type, date range
- Read-only: All fields except status

#### OrderAdmin (Updated)
- Added `SMSNotificationInline` to show SMS history

## Configuration

### Step 1: Install Dependencies
```bash
pip install twilio
```

### Step 2: Get Twilio Account
Visit https://www.twilio.com
- Sign up for free account
- Verify your phone number
- Get a trial phone number

### Step 3: Set Environment Variables

**Windows PowerShell:**
```powershell
$env:TWILIO_ACCOUNT_SID = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
$env:TWILIO_AUTH_TOKEN = "auth_token_here"
$env:TWILIO_PHONE_NUMBER = "+1234567890"
```

**Windows CMD:**
```cmd
set TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
set TWILIO_AUTH_TOKEN=auth_token_here
set TWILIO_PHONE_NUMBER=+1234567890
```

**Linux/Mac (.bashrc or .zshrc):**
```bash
export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export TWILIO_AUTH_TOKEN="auth_token_here"
export TWILIO_PHONE_NUMBER="+1234567890"
```

### Step 4: Persistent Configuration (.env file)

Create `.env` in project root:
```
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=auth_token_here
TWILIO_PHONE_NUMBER=+1234567890
```

Install python-dotenv:
```bash
pip install python-dotenv
```

Update settings.py:
```python
from dotenv import load_dotenv
import os

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
```

## Usage

### For Customers
1. When adding to cart, proceed to checkout
2. Fill in all shipping details including phone number
3. **Phone format must include country code** (e.g., +1 for USA)
4. Complete order
5. Receive SMS confirmation automatically

### For Admins

#### Via Django Admin
1. Go to `/admin/about/order/`
2. Click on an order
3. Scroll to "SMS Notifications" section
4. Click "Add" to manually send new notifications

#### Via Command Line
```bash
# Send order confirmation
python manage.py send_sms_notification --order-id=1 --type=confirmation

# Send shipped notification
python manage.py send_sms_notification --order-id=1 --type=shipped

# Send delivered notification
python manage.py send_sms_notification --order-id=1 --type=delivered

# Send custom SMS
python manage.py send_sms_notification --phone="+1234567890" --message="Hey! Your code is SUMMER20"
```

#### Via Python
```python
from about.sms_service import send_order_confirmation_sms
from about.models import Order

order = Order.objects.get(id=1)
success = send_order_confirmation_sms(order)
print(f"SMS sent: {success}")
```

## SMS Message Templates

### Order Confirmation
```
Order Confirmation ✓

Order #: ORD-20260401120000-1234
Items: 2x Widget A, 1x Widget B
Total: $99.99
Status: Pending

Your order will be shipped to:
123 Main St
New York, NY 10001

Thank you for your purchase!
```

### Order Shipped
```
Your order has been shipped! 📦

Order #: ORD-20260401120000-1234
Estimated Delivery: 3-5 business days
Total: $99.99

Track your order and manage preferences in your account.

Thank you!
```

### Order Delivered
```
Your order has been delivered! ✓

Order #: ORD-20260401120000-1234
Total: $99.99

We'd love to hear from you! Please leave a review.

Thank you for shopping with us!
```

## Phone Number Format

Always include country code:

| Country | Format | Example |
|---------|--------|---------|
| USA | +1 | +11234567890 |
| UK | +44 | +441234567890 |
| India | +91 | +911234567890 |
| Canada | +1 | +11234567890 |
| Australia | +61 | +611234567890 |

## Twilio Pricing

| Item | Cost |
|------|------|
| Free Trial Credit | $15 |
| Per SMS (US) | ~$0.0075 |
| SMS with $15 credit | ~2000 |

Trial restrictions:
- Can only send to verified phone numbers
- Upgrade to production to send to any number

## Error Handling

### SMS Disabled
If SMS credentials aren't configured, the system:
- Logs: "SMS is not enabled"
- Records failure in SMSNotification
- Shows success message to customer anyway
- Does NOT crash the order process

### Failed SMS
Common failure reasons:
- Invalid phone number format
- Twilio credentials incorrect
- Insufficient credit
- Network error

All failures are logged:
- Django logs
- SMSNotification model (status='failed')

## Monitoring & Logging

### Django Admin
1. Go to `/admin/about/smsnotification/`
2. View all SMS messages
3. Filter by status, type, date
4. Click to see full message and order details

### Django Logs
```
python manage.py runserver
# Check console for SMS success/failure messages
```

### Twilio Dashboard
1. Log in to console.twilio.com
2. Navigate to "Logs" → "Messages"
3. View all SMS delivery status
4. Check for failures or issues

## Testing

### Local Testing
1. Set environment variables (see Config section)
2. Start server: `python manage.py runserver`
3. Create test product
4. Add to cart, proceed to checkout
5. Use test phone: `+15005550006` (Twilio test number)
6. Complete order
7. Check console for SMS status

### Production Testing
1. Upgrade Twilio to paid account
2. Use real phone number
3. Verify SMS arrives within seconds
4. Check SMSNotification in admin

## Troubleshooting

### Problem: SMS not sending
**Solution 1 - Check environment variables**
```bash
# Windows PowerShell
echo $env:TWILIO_ACCOUNT_SID

# Linux/Mac
echo $TWILIO_ACCOUNT_SID
```

**Solution 2 - Verify phone format**
- Must start with + and country code
- Example: +1 (US), +44 (UK), +91 (India)

**Solution 3 - Check Django logs**
Look for error messages in console

### Problem: Invalid credentials error
Re-verify credentials from Twilio dashboard:
1. Account SID starts with `AC`
2. Auth Token is long string
3. Phone number has + prefix
4. All copied correctly

### Problem: SMS shows as failed in admin
1. Check SMSNotification status = "failed"
2. Review error in Django logs
3. Click Twilio SID link to check Twilio dashboard
4. May be trial account restriction

## Files Modified/Created

### New Files
- `about/sms_service.py` - SMS service functions
- `about/management/commands/send_sms_notification.py` - Management command
- `about/migrations/0005_smsnotification.py` - Database migration
- `SMS_SETUP.md` - Setup guide
- `SMS_QUICK_START.md` - Quick start

### Modified Files
- `about/models.py` - Added SMSNotification model
- `about/views.py` - Added SMS import and calling in checkout
- `about/admin.py` - Added SMS admin interface
- `lucifer/settings.py` - Added Twilio configuration
- `templates/order_confirmation.html` - Display SMS info

## Best Practices

1. **Security**
   - Never commit credentials to repository
   - Use .env files with .gitignore
   - Keep Auth Token secret

2. **Reliability**
   - Always verify phone format
   - Monitor SMS delivery
   - Have fallback communication method

3. **Customer Experience**
   - Clear messaging
   - Professional tone
   - Include order number for reference

4. **Cost Management**
   - Monitor Twilio spending
   - Plan message types
   - Upgrade when needed

## API Reference

### send_order_confirmation_sms(order)
Send order confirmation SMS
```python
from about.sms_service import send_order_confirmation_sms
from about.models import Order

order = Order.objects.get(id=1)
success = send_order_confirmation_sms(order)
# Returns: True/False
```

### send_order_shipped_sms(order)
Send shipped notification
```python
success = send_order_shipped_sms(order)
```

### send_order_delivered_sms(order)
Send delivered notification
```python
success = send_order_delivered_sms(order)
```

### send_custom_sms(phone_number, message_text)
Send custom message
```python
success = send_custom_sms("+1234567890", "Your custom message")
```

## Support & Resources

- **Twilio Docs**: https://www.twilio.com/docs
- **Twilio Console**: https://console.twilio.com/auth
- **Django Docs**: https://docs.djangoproject.com/
- **GitHub Issues**: Create issue in your repo

---

**SMS Notification System v1.0** - Ready for production use!
