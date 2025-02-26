from source.sound import play_alert_sound
from source.message import send_alert_sms
from source.buzzer import send_buzzer_signal

def handle_alert(esp, animal):
    """Triggers necessary alerts when a wild animal is detected."""
    play_alert_sound()
    send_alert_sms(animal)
    send_buzzer_signal(esp, True)
