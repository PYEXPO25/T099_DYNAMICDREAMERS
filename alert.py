from sound import play_alert_sound
from message import send_alert_sms
from buzzer import send_buzzer_signal

def handle_alert(esp, animal):
    """Triggers necessary alerts when a wild animal is detected."""
    play_alert_sound()
    send_alert_sms(animal)
    send_buzzer_signal(esp, True)
