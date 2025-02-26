from twilio.rest import Client

# Twilio Credentials
TWILIO_SID = "AC6c8c93e674d3a459e7b0094c2693e207"
TWILIO_AUTH_TOKEN = "633183fcf84353024b5407124ad4afcf"
TWILIO_PHONE_NUMBER = "+12765826565"
USER_PHONE_NUMBER = "+916380666797"

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_alert_sms(animal):
    """Send SMS alert when a wild animal is detected."""
    client.messages.create(
        body=f"🚨 Alert! Wild animal detected: {animal}. Stay Safe!",
        from_=TWILIO_PHONE_NUMBER,
        to=USER_PHONE_NUMBER
    )
    print("📩 SMS Alert Sent!")
