import serial
import time

def connect_esp32(port="COM5", baud_rate=115200):
    """Establish connection with ESP32."""
    try:
        esp = serial.Serial(port, baud_rate, timeout=1)
        time.sleep(2)
        print("ESP32 Connected Successfully!")
        return esp
    except Exception as e:
        print(f"Error connecting to ESP32: {e}")
        return None

def send_buzzer_signal(esp, state):
    """Send signal to ESP32 for buzzer alert."""
    if esp:
        signal = b"1\n" if state else b"0\n"
        esp.write(signal)
        print(f"🔴 Sent to ESP32: {signal.strip().decode()}")
