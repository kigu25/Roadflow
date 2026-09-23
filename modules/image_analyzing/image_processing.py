from ultralytics import YOLO
import cv2
from modules.image_analyzing.insert_analysis_detection_db import insert_detections_db, insert_analysis_db
from modules.image_handling.save_image import save_image

model = YOLO("yolo26x.pt")


def image_processing(image_filepath, camera_id, photo_id, photo_time_obj):

    processed_image = model(image_filepath, conf=0.49, imgsz=1280)
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

        annotated = result.plot()
        success, encoded_image = cv2.imencode(".jpg", annotated)
        if not success:
            print("Could not encode the image\n", " ", "analyzed image is not saved to image_storage")
        else:
            image_bytes = encoded_image.tobytes()
            analyzed_filepath = save_image(image_bytes, camera_id, photo_time_obj, image_type="analyzed")
    

    analysis_id = insert_analysis_db(photo_id, nr_vehicles, analyzed_filepath)
    insert_detections_db(analysis_id, all_detections)