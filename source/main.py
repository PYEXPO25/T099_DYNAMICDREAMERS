from PyQt6.QtWidgets import QApplication
from source.ui import WildAnimalDetector

app = QApplication([])
window = WildAnimalDetector()
window.show()
app.exec()
#pip install -r requirements.txt
#python main.py
