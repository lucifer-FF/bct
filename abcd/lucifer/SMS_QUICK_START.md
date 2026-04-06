# SMS Feature - Quick Start Guide

## What's New
Your ecommerce platform now sends **automatic SMS confirmations** to customers when they place orders!

## Features

✅ **Automatic Order Confirmation SMS**
- Sends immediately after order is placed
- Includes: Order number, items, total, shipping address
- Sent to customer's phone number

✅ **SMS Tracking**
- View all SMS messages sent in Django Admin
- Track delivery status (sent/failed)
- See Twilio delivery SIDs

✅ **Additional Notifications** (Manual/Admin)
- Order shipped notification
- Order delivered notification
- Custom marketing SMS

✅ **Management Command**
- Send SMS from command line
- Retry failed messages
- Custom SMS campaigns

## Setup (Important!)

### Step 1: Get Twilio Account
1. Go to https://www.twilio.com
2. Sign up (free trial with $15 credit)
3. Verify your phone number
4. Get a trial phone number

### Step 2: Get Your Credentials
From Twilio Console (https://console.twilio.com/):
- **Account SID**: Starts with `AC...`
- **Auth Token**: Keep this secret!
- **Phone Number**: Your Twilio number (e.g., +1XXXXXXXXXX)

### Step 3: Set Environment Variables

**On Windows (PowerShell):**
```powershell
$env:TWILIO_ACCOUNT_SID = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
$env:TWILIO_AUTH_TOKEN = "your_auth_token_here"
$env:TWILIO_PHONE_NUMBER = "+1234567890"
```

**On Windows (Command Prompt):**
```cmd
set TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
set TWILIO_AUTH_TOKEN=your_auth_token_here
set TWILIO_PHONE_NUMBER=+1234567890
```

**On Linux/Mac:**
```bash
export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export TWILIO_AUTH_TOKEN="your_auth_token_here"
export TWILIO_PHONE_NUMBER="+1234567890"
```

### Step 4: Test It!
1. Start Django server: `python manage.py runserver`
2. Create a product
3. Add to cart and checkout
4. Enter your phone number (with country code, e.g., +1)
5. Check your phone for SMS!

## File Structure

```
about/
├── models.py                               # SMSNotification model
├── sms_service.py                         # SMS functions (NEW)
├── views.py                               # Updated with SMS
├── admin.py                               # SMS tracking in admin
├── management/
│   └── commands/
│       └── send_sms_notification.py       # Management command (NEW)

lucifer/
└── settings.py                            # SMS configuration (NEW)

SMS_SETUP.md                               # Detailed setup guide
```

## Usage Examples

### From Command Line
```bash
# Send confirmation SMS for order ID 1
python manage.py send_sms_notification --order-id=1 --type=confirmation

# Send shipped notification
python manage.py send_sms_notification --order-id=1 --type=shipped

# Send delivered notification
python manage.py send_sms_notification --order-id=1 --type=delivered

# Send custom SMS
python manage.py send_sms_notification --phone="+1234567890" --message="Your custom message"
```

### From Django Admin
1. Go to `/admin/`
2. Navigate to **SMS Notifications**
3. View all sent messages with status
4. Click on order to see associated SMS

### From Python Code
```python
from about.sms_service import send_order_confirmation_sms
from about.models import Order

order = Order.objects.get(id=1)
send_order_confirmation_sms(order)
```

## SMS Content

### Order Confirmation (Auto)
```
Order Confirmation ✓

Order #: ORD-20260401120000-1234
Items: 2x Product A, 1x Product B
Total: $99.99
Status: Pending

Your order will be shipped to:
123 Main Street
New York, NY 10001

Thank you for your purchase!
```

### Order Shipped (Manual)
```
Your order has been shipped! 📦

Order #: ORD-20260401120000-1234
Estimated Delivery: 3-5 business days
Total: $99.99

Track your order and manage preferences in your account.

Thank you!
```

### Order Delivered (Manual)
```
Your order has been delivered! ✓

Order #: ORD-20260401120000-1234
Total: $99.99

We'd love to hear from you! Please leave a review.

Thank you for shopping with us!
```

## Important Notes

### Phone Number Format
- Must include country code
- US: `+1234567890`
- UK: `+441234567890`
- India: `+911234567890`

### Twilio Free Trial
- $15 starting credit
- SMS costs ~$0.0075 each
- ~2000 SMS with free credits
- During trial, can only send to verified numbers

### Troubleshooting

**SMS not sending?**
1. Check environment variables are set: `echo $env:TWILIO_ACCOUNT_SID`
2. Verify phone format includes country code
3. Check Django logs for errors
4. Verify Twilio credentials in dashboard

**Check SMS Status**
- Admin Panel → SMS Notifications
- Look for "Sent" or "Failed" status
- View Twilio SID for support

**Force Resend Message**
```bash
python manage.py send_sms_notification --order-id=1 --type=confirmation
```

## Security Notes
- Never commit `.env` files with credentials
- Keep Auth Token secret
- Use environment variables in production
- Check Twilio dashboard for API activity

## Next Steps
1. Set up your Twilio account
2. Configure environment variables
3. Test with a real order
4. Monitor SMS Notifications in admin
5. Set up automated notifications for shipped/delivered

## Support
- Twilio Docs: https://www.twilio.com/docs
- Django Logs: `manage.py` output
- Check SMS Notifications in Admin for status

---

**That's it!** Your SMS notification system is ready to use. Every new order will automatically notify customers! 📱
