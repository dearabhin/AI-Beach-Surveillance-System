import cv2
from ultralytics import YOLO

# Load pre-trained YOLO model
model = YOLO("yolov8n.pt")

def detect_people(video_path):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Perform object detection
        results = model(frame)

        # Annotate frame
        annotated_frame = results[0].plot()
        cv2.imshow("Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Example usage
detect_people("data/videos/beach.mp4")
