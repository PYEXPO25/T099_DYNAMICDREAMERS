from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("C://Users//ragav//OneDrive//Documents//Wild_Animal_Detection//Data_Files//yolov8m.pt")

# Wild animal classes
WILD_ANIMAL_CLASSES = {
    "elephant", "bear", "zebra", "giraffe", "lion", "tiger", "leopard", "cheetah", "wolf", "fox",
    "panther", "jaguar", "coyote", "hyena", "rhinoceros", "hippopotamus", "buffalo", "deer", "moose",
    "bison","goat","pig",
}

def detect_animals(frame):
    """Detect wild animals in the given frame using YOLOv8."""
    results = model(frame, conf=0.6)
    detected_animal = None
    wild_animal_detected = False

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            if class_name in WILD_ANIMAL_CLASSES:
                wild_animal_detected = True
                detected_animal = class_name
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                cv2.putText(frame, class_name, (x1, y1 - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 3)

    return wild_animal_detected, detected_animal, frame
