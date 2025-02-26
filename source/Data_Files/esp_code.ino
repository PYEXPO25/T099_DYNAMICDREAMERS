#define BUZZER_PIN 5  // Buzzer connected to GPIO5

void setup() {
    Serial.begin(115200);
    pinMode(BUZZER_PIN, OUTPUT);
    Serial.println("ESP32 Ready!");
}

void loop() {
    if (Serial.available()) {
        char command = Serial.read();  // Read command from Python

        if (command == '1') {
            Serial.println("🚨 Wild animal detected! Activating buzzer...");
            digitalWrite(BUZZER_PIN, HIGH);
            delay(2000);  // Buzzer ON for 2 seconds
            digitalWrite(BUZZER_PIN, LOW);
        } else if (command == '0') {
            Serial.println("✅ No wild animal detected. Buzzer OFF.");
            digitalWrite(BUZZER_PIN, LOW);
        }
    }
}
