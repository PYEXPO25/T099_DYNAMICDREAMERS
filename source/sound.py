import pygame

# Initialize pygame mixer
pygame.mixer.init()
ALERT_SOUND_PATH = "C://Users//ragav//OneDrive//Documents//Wild_Animal_Detection//Data_Files//alert_cracker.mp3"

def play_alert_sound():
    """Plays the alert sound when a wild animal is detected."""
    pygame.mixer.music.load(ALERT_SOUND_PATH)
    pygame.mixer.music.play()
    print("🔊 Playing Cracking Sound!")
