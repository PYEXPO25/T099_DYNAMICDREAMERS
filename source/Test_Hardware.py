import serial
import time

esp = serial.Serial('COM3', 115200, timeout=1)  # Change COM port if needed
time.sleep(2)

esp.write(b'1')  # Send command to ESP32
print("Buzzer triggered!")
