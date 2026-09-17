from modules.camera_setup.build_set_config import build_set
from modules.trafikverket_api.get_all_cameras import get_all_cameras

def match_cameras():
    filter_set = build_set()
    data = get_all_cameras()

    
    for x in data:
        name = x['Name']
        id = x['Id']
        geo = x['Geometry']['SWEREF99TM']

        if name in filter_set:
            print("SUCCESS: " + name)
    
    

    