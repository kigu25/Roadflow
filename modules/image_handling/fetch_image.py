import requests
from modules.camera_setup.get_camera_data import get_camera_data
from modules.image_handling.save_image import save_image
from modules.image_handling.insert_image_db import insert_image_db
from modules.timezone_convert import timezone_convert


def fetch_image():

    camera_data = get_camera_data()

    for camera in camera_data:
        camera_id = camera['Id']
        photo_time = camera['PhotoTime']

        #Fallback if fullsize does not exist for that specific camera
        if camera.get("PhotoUrlFullsize"):
            photo_link = camera['PhotoUrlFullsize']
        else:
            photo_link = camera['PhotoUrl']

        fetched_img = requests.get(photo_link).content

        photo_time_obj = timezone_convert(photo_time)

        filepath = save_image(fetched_img, camera_id, photo_time_obj)
        insert_image_db(camera_id, photo_time_obj, filepath)