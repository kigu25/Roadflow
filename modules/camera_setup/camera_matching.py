from modules.camera_setup.build_camera_set import build_set
from modules.trafikverket_api.get_all_cameras import get_all_cameras
from database_queries.insert_camera_db import insert_camera_db
import json

def camera_matching():
    filter_set = build_set()
    data = get_all_cameras()

    #Cameras with duplicate names but different id's
    excluded_ids = {
        "SE_STA_CAMERA_0_1075001079",
        "SE_STA_CAMERA_0_1075001074",
        "SE_STA_CAMERA_0_1075001168"
    }


    matched = []
    
    for camera in data:
        name = camera['Name']
        camera_id = camera['Id']
        geo = camera['Geometry']['WGS84']


        if name in filter_set and camera_id not in excluded_ids:
            matched.append({
                "name" : name,
                "id" : camera_id,
                "geo" : geo,
            })

    with open("camera_configs/confirmed_cameras.json", "w", encoding="utf-8") as file:
        json.dump(matched, file, ensure_ascii=False, indent=2)

    insert_camera_db(matched)