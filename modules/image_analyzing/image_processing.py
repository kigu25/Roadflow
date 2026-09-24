from ultralytics import YOLO
import cv2

model = YOLO("yolo26x.pt")


def image_processing(image_filepath, conf_value = 0.42, test=False):

    processed_image = model(image_filepath, conf=conf_value, imgsz=1280, verbose=False, augment=True, classes=[1,2,3,5,7])

    all_detections_list = []

    for result in processed_image:
        boxes = result.boxes
        nr_vehicles = len(boxes)

        for box in boxes:
            identification_id = int(box.cls)
            vehicle = result.names[identification_id]

            conf = round(float(box.conf), 3)

            coord = box.xyxy[0]
            x1, y1, x2, y2 = coord.tolist()

            all_detections_list.append({
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
            print("\n" "Number of detections", nr_vehicles, "\n")
            print( "All detections:")

            for x in all_detections_list:
                print(x['vehicle'], " ", x["confident"])

            result.show()

    return image_bytes, all_detections_list, nr_vehicles