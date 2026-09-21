from modules.camera_setup.build_set_config import build_set
from modules.trafikverket_api.get_all_cameras import get_all_cameras
import json

def camera_matching():
    filter_set = build_set()
    data = get_all_cameras()

    matched = []
    
    for camera in data:
        name = camera['Name']
        camera_id = camera['Id']
        geo = camera['Geometry']['WGS84']
        time = camera['PhotoTime']

        if camera.get("PhotoUrlFullsize"):
            photo = camera['PhotoUrlFullsize']   
        else:
            photo = camera['PhotoUrl']

        
        if name in filter_set:
            matched.append({
                "name" : name,
                "id" : camera_id,
                "geo" : geo,
                "time" : time,
                "photo" : photo
            })

    with open("camera_configs/confirmed_cameras.json", "w", encoding="utf-8") as file:
        json.dump(matched, file, ensure_ascii=False, indent=2)