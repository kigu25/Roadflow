from ultralytics import YOLO
from modules.image_analyzing.insert_analysis_detection_db import insert_detections_db, insert_analysis_db

model = YOLO("yolo26x.pt")


def image_processing(image, photo_id = 1, photo_time_obj = 1000): #REMOVE DEFAULT VALUES AFTER TESTS

    processed_image = model(image, conf=0.49, imgsz=1280)
    all_detections = []

    for result in processed_image:
        boxes = result.boxes
        nr_vehicles = len(boxes)

        for box in boxes:
            identification_id = int(box.cls)
            vehicle = result.names[identification_id]

            conf = round(float(box.conf), 3)

            coord = box.xyxy[0]
            x1, y1, x2, y2 = coord.tolist()

            all_detections.append({
                "vehicle" : vehicle,
                "confident" : conf,
                "x1" : x1,
                "y1" : y1,
                "x2" : x2,
                "y2" : y2
            })


    filepath = ""

    analysis_id = insert_analysis_db(photo_id, nr_vehicles, filepath)
    insert_detections_db(analysis_id, all_detections)