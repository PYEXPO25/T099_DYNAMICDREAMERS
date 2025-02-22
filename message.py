from twilio.rest import Client

# Twilio Credentials
TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""
TWILIO_PHONE_NUMBER = ""
USER_PHONE_NUMBER = ""

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_alert_sms(animal):
    """Send SMS alert when a wild animal is detected."""
    client.messages.create(
        body=f"🚨 Alert! Wild animal detected: {animal}. Stay Safe!",
        from_=TWILIO_PHONE_NUMBER,
        to=USER_PHONE_NUMBER
    )
    print("📩 SMS Alert Sent!")
