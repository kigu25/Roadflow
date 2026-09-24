from ultralytics import YOLO
import cv2

model = YOLO("yolo26x.pt")


def image_processing(image_filepath,  test=False):

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

        image_bytes = None

        if test == False:
            annotated = result.plot()
            success, encoded_image = cv2.imencode(".jpg", annotated)
            image_bytes = encoded_image.tobytes()
        else:
            result.show()

    return image_bytes, all_detections, nr_vehicles