from modules.image_handling.get_camera_data import get_camera_data
from modules.image_handling.fetch_image import fetch_image
from modules.utils.timezone_convert import timezone_convert
from modules.image_handling.save_image import save_image
from modules.image_analyzing.image_processing import image_processing
from modules.image_handling.insert_image_db import insert_image_db



def img_handling_pipeline():

    camera_data_list = get_camera_data()


    for camera in camera_data_list:
        camera_id = camera['Id']

        image = fetch_image(camera)

        photo_time_obj = timezone_convert(camera['PhotoTime'])

        filepath = save_image(image, camera_id, photo_time_obj, "original")

        photo_id = insert_image_db(camera_id, photo_time_obj, filepath)

        image_processing(filepath, camera_id, photo_id, photo_time_obj)