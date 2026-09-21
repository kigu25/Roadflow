import requests
from modules.image_handling.build_links import build_links
from modules.image_handling.save_image import save_image


def fetch_image():

    link_data = build_links()

    for camera in link_data:
        camera_id = camera['id']
        photo_time = camera['photo_time']
        photo_link = camera['photo_link']

        fetched_img = requests.get(photo_link).content

        save_image(fetched_img, camera_id, photo_time)