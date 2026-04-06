# Twilio Credentials Verification Guide

## Issue: Authentication Error (Error 20003)
Your SMS sending is failing with Twilio authentication error. This means the credentials may be incorrect or malformed.

## Quick Verification Steps

### Step 1: Check Twilio Dashboard
1. Go to https://console.twilio.com/
2. Log in with your Twilio account
3. Click your **Account SID** at the bottom left

### Step 2: Verify Your Credentials

**What you should see:**
- **Account SID**: 4-letter project name visible in dashboard (like "AC" followed by 32 hex characters)
- **Auth Token**: Shown only once when account created (hidden after that)
- **Phone Number**: Your Twilio number (e.g., +1234567890)

### Step 3: Get Correct Credentials

If you can't find Auth Token:
1. Go to https://console.twilio.com/
2. Click **Account** menu (bottom left)
3. Click **API keys & tokens**
4. Under "Auth Tokens", click **Show** to reveal current token
5. If you forgot it, use **Rotate to generate new token**

### Step 4: Verify Phone Number

1. In Twilio console
2. Go to **Phone Numbers** → **Manage**
3. Click on your number
4. Copy the full number with country code (e.g., +917001945496)

## Common Issues

### Issue #1: Auth Token Invalid
**Symptom**: Error 20003 Authenticate
**Cause**: Wrong or expired token
**Fix**: Generate new token in Twilio console

### Issue #2: Account SID Typo
**Symptom**: Error 20003 Authenticate
**Cause**: Copied incorrectly or API key instead of Account SID
**Fix**: Use Account SID (not API Key or other credentials)

### Issue #3: Phone Number Not Verified
**Symptom**: SMS fails or shows invalid number
**Cause**: Number not added to account
**Fix**: Verify number in Twilio console

### Issue #4: Trial Account Limitations
**Symptom**: SMS to unverified numbers fails
**Cause**: Trial account can only send to verified numbers
**Fix**: Add phone number to verified caller IDs in Twilio console

## How to Reset Credentials in PowerShell

Once you have verified credentials:

```powershell
# Set environment variables (replace with YOUR actual credentials)
$env:TWILIO_ACCOUNT_SID = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
$env:TWILIO_AUTH_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
$env:TWILIO_PHONE_NUMBER = "+917001945496"

# Verify they're set
echo $env:TWILIO_ACCOUNT_SID
echo $env:TWILIO_AUTH_TOKEN
echo $env:TWILIO_PHONE_NUMBER

# Test SMS
python manage.py send_sms_notification --phone="+917001945496" --message="Test"
```

## Current Credentials Status

### What You Set:
```
TWILIO_ACCOUNT_SID = AC3345eca7f6c10a91608174d9d1bccc94
TWILIO_AUTH_TOKEN = US6cbefbcbf2018de9e613380179217582
TWILIO_PHONE_NUMBER = +917001945496
```

⚠️ **Issue Detected**: Auth Token format looks unusual. Twilio Auth Tokens typically start with "auth" or are long hex strings without "US" prefix.

### What to Check:
1. **Verify in Twilio Console**: Go to Account → API keys & tokens
2. **Look for "Auth Token"**: Not "API Key" or other values
3. **Copy exactly**: Make sure no extra spaces
4. **Don't paste from email**: Type directly from console

## Next Steps

1️⃣ Verify credentials in Twilio console (link above)
2️⃣ Check Auth Token format (shouldn't start with "US")
3️⃣ Reset environment variables with correct values
4️⃣ Run test again: `python manage.py send_sms_notification --phone="+917001945496" --message="Test"`
5️⃣ If still failing, regenerate token in Twilio console

---

Need help? Check Twilio documentation:
https://www.twilio.com/docs/sms/send-messages

Or view your test SMS logs:
http://localhost:8000/admin/about/smsnotification/
