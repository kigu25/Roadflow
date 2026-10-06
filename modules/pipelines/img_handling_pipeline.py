from modules.image_handling.get_camera_data import get_camera_data
from modules.image_handling.fetch_image import fetch_image
from modules.utils.timezone_convert import timezone_convert
from modules.image_handling.save_image import save_image
from modules.image_analyzing.image_processing import image_processing
from database_queries.insert_image_db import insert_image_db
from database_queries.insert_detection_db import insert_detections_db
from database_queries.insert_analysis_db import insert_analysis_db
from database_queries.latest_timestamp_camera import get_latest_timestamp_cam
from modules.utils.camera_id_converter import camera_id_converter

from database_queries import data_gap_queries


def img_handling_pipeline():

    camera_data_list = get_camera_data()

    for camera in camera_data_list:
        camera_id = camera_id_converter(camera['Id'])

        try:
            camera_active = camera['Active']

            if not camera_active:
                print(f"Camera with id: {camera_id} is not active according to trafikverket API, Logging data_gap in DB.")
                data_gap_queries.create_gap(camera_id, "Camera not active from API")
                continue

            #Checking if timestamp is same before fetching image
            photo_time_obj = timezone_convert(camera['PhotoTime'])
            latest_timestamp = get_latest_timestamp_cam(camera_id)

            if latest_timestamp is not None and photo_time_obj <= latest_timestamp:
                print(f"Camera with id: {camera_id} has stopped updating. Logging data_gap in DB.")
                data_gap_queries.create_gap(camera_id, "Timestamp not updated.")
                continue


            image = fetch_image(camera)
            if image is None:
                print(f"Failed to fetch image for camera with ID: {camera_id}. data_gap logged in DB.")
                data_gap_queries.create_gap(camera_id, "Failed to fetch image.")
                continue


            filepath = save_image(image, camera_id, photo_time_obj, "original")
            photo_id = insert_image_db(camera_id, photo_time_obj, filepath)


            gap_id = data_gap_queries.check_for_gap(camera_id)
            if gap_id != None:
                data_gap_queries.end_gap(gap_id)


            #Analyzing the fetched image
            image_b, all_detections, nr_vehicles = image_processing(filepath)

            analyzed_filepath = save_image(image_b, camera_id, photo_time_obj, image_type="analyzed")

            analysis_id = insert_analysis_db(photo_id, nr_vehicles, analyzed_filepath)

            insert_detections_db(analysis_id, all_detections)


        except Exception as excepetionn:
            print(f"Camera: {camera_id} failed: {excepetionn}")
            
            try:
                data_gap_queries.create_gap(camera_id, "pipeline error.")
            except Exception as db_erorr:
                print(f"Could not log data_gap. CODE: {db_erorr}")

            continue