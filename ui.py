import cv2
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QImage, QPixmap, QFont
from PyQt6.QtCore import QTimer, Qt
from detection import detect_animals
from alert import handle_alert
from buzzer import connect_esp32, send_buzzer_signal

class WildAnimalDetector(QWidget):
    def __init__(self):
        super().__init__()

        # ESP32 Serial Connection
        self.esp = connect_esp32()

        # Open Webcam
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Error: Could not open webcam.")
            exit()

        self.last_state = False

        # UI Initialization
        self.init_ui()

    def init_ui(self):
        """Initialize Modern UI Layout"""
        self.setWindowTitle("Wild Animal Detection - AI Powered")
        self.setGeometry(200, 100, 1000, 750)
        self.setStyleSheet("""
               QWidget {
                background-color: #1e1e1e;
                color: white;
                font-family: Arial;
            }
            QLabel {
                font-size: 18px;
            }
            QPushButton {
                background-color: #ff4c4c;
                color: white;
                border-radius: 8px;
                padding: 12px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #ff1a1a;
            }
        """)

   # Video Display (Centered, Fixed Size)
        self.video_label = QLabel(self)
        self.video_label.setFixedSize(600, 400)
        self.video_label.setStyleSheet("border: 4px solid white; border-radius: 10px; background-color: black;")

   # Detected Class Display (Above Alert Box)
        self.class_label = QLabel("Detected: None", self)
        self.class_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.class_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        self.class_label.setStyleSheet("background-color: #2e2e2e; padding: 12px; border-radius: 8px;")

   # Alert Frame (Below Detected Class)
        self.alert_box = QLabel("⚠ ALERT: Wild Animal Detected!", self)
        self.alert_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.alert_box.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        self.alert_box.setStyleSheet("background-color: #ff4c4c; padding: 20px; border-radius: 10px; color: white;")
        self.alert_box.hide()

        # Exit Button (Below Alert Box)
        self.exit_btn = QPushButton("Exit", self)
        self.exit_btn.clicked.connect(self.close)
        self.exit_btn.setFixedSize(120, 50)

              # Layout (Reordered)
        main_layout = QVBoxLayout()
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        main_layout.addWidget(self.video_label, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.class_label, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.alert_box, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.exit_btn, alignment=Qt.AlignmentFlag.AlignCenter)  # Exit button at the bottom
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.setLayout(main_layout)

        # Start Timer to Update Frames
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def update_frame(self):
        """Capture and Process Video Frame"""
        ret, frame = self.cap.read()
        if not ret:
            return

        detected, animal, frame = detect_animals(frame)
        self.class_label.setText(f"Detected: {animal if detected else 'None'}")

        if detected and detected != self.last_state:
            handle_alert(self.esp, animal)

        self.last_state = detected
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        qimg = QImage(frame.data, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format.Format_RGB888)
        self.video_label.setPixmap(QPixmap.fromImage(qimg))
