import json

def build_links():
    links = []

    with open("camera_configs/confirmed_cameras.json", "r", encoding="UTF-8") as f:
        cameras = json.load(f)

    for x in cameras:
        links.append({
            "id" : x['id'],
            "photo_time" : x['photo_time'],
            "photo_link" : x['photo_link']
        })

    return links