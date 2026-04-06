# SMS Configuration Guide (Twilio)

## Overview
This ecommerce system includes SMS notification support using Twilio. Customers will receive order confirmation messages via SMS.

## Setup Instructions

### 1. Get Twilio Account
- Visit https://www.twilio.com
- Sign up for a free account (includes free trial credits)
- Verify your phone number
- Request a trial phone number (this will be your sender ID)

### 2. Get Credentials
After creating your Twilio account:
1. Go to Dashboard (https://console.twilio.com/auth)
2. Find your:
   - **Account SID** (starts with AC...)
   - **Auth Token** (keep this secret!)
   - **Phone Number** (Twilio number you got in trial setup)

### 3. Configure Environment Variables

**For Local Development (Windows):**
```powershell
$env:TWILIO_ACCOUNT_SID = "your_account_sid_here"
$env:TWILIO_AUTH_TOKEN = "your_auth_token_here"
$env:TWILIO_PHONE_NUMBER = "+1XXXXXXXXXX"  # Your Twilio phone number
```

**For Windows Command Prompt:**
```cmd
set TWILIO_ACCOUNT_SID=your_account_sid_here
set TWILIO_AUTH_TOKEN=your_auth_token_here
set TWILIO_PHONE_NUMBER=+1XXXXXXXXXX
```

**For Linux/Mac:**
```bash
export TWILIO_ACCOUNT_SID="your_account_sid_here"
export TWILIO_AUTH_TOKEN="your_auth_token_here"
export TWILIO_PHONE_NUMBER="+1XXXXXXXXXX"
```

### 4. Permanent Setup (Recommended)

Create a `.env` file in your project root:
```
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=+1XXXXXXXXXX
```

Then install `python-dotenv`:
```bash
pip install python-dotenv
```

Update settings.py to load from .env:
```python
from dotenv import load_dotenv
import os

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
```

### 5. Testing SMS

Run the Django development server and test by:
1. Creating a product
2. Adding to cart
3. Proceeding to checkout
4. Entering your phone number
5. Completing the order
6. Check your phone for SMS confirmation

## SMS Features

### Order Confirmation (On Checkout)
- Sent automatically after order placement
- Includes: Order number, items, total, shipping address

### Order Status Updates (Manual)
When you update order status in Django admin, you can manually trigger:
- **Shipped** notification
- **Delivered** notification

### Custom SMS
Admin users can send custom SMS to customers for promotions or updates.

## Important Notes

- **Free Tier**: Twilio free trial includes $15 credits. One SMS typically costs $0.0075
- **Phone Format**: Always include country code (e.g., +1 for US, +44 for UK)
- **Trial Limitations**: During trial, SMS can only be sent to verified numbers
- **Production**: No restrictions once upgraded to paid account

## Troubleshooting

### SMS Not Sending
1. Check environment variables are set correctly
2. Verify phone number format includes country code
3. Check console logs for errors
4. Confirm Twilio credentials are valid

### Check Status
Look for SMS status in Django logs:
- Success: "SMS sent successfully for order..."
- Error: "Failed to send SMS for order..."

## File Structure
- `about/sms_service.py` - SMS service functions
- `about/views.py` - Integrated SMS sending in checkout
- `lucifer/settings.py` - SMS configuration

## Support
For issues:
1. Check Twilio dashboard for failed messages
2. Review Django error logs
3. Verify environment variables are loaded
