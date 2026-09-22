import requests
from modules.image_handling.build_links import build_links
from modules.image_handling.save_image import save_image
from modules.image_handling.insert_image_db import insert_image_db
from modules.timezone_convert import timezone_convert


def fetch_image():

    link_data = build_links()

    for camera in link_data:
        camera_id = camera['id']
        photo_time = camera['photo_time']
        photo_link = camera['photo_link']

        fetched_img = requests.get(photo_link).content

        photo_time_obj = timezone_convert(photo_time)

        filepath = save_image(fetched_img, camera_id, photo_time_obj)
        insert_image_db(camera_id, photo_time_obj, filepath)