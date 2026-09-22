import os
import json
import requests

def get_camera_data():
    api_key = os.getenv("trafikverket_api_key")
    url = "https://api.trafikinfo.trafikverket.se/v2/data.json"


    all_ids = []
    with open("camera_configs/confirmed_cameras.json", "r") as f:
        confirmed_cameras = json.load(f)

        for x in confirmed_cameras:
            all_ids.append(x['id'])


    camera_info = []
    for camera_id in all_ids:

        message = "<REQUEST>" \
                        f"<LOGIN authenticationkey='{api_key}'/>" \
                        f"<QUERY objecttype='Camera' namespace='road.infrastructure' schemaversion='1.1' limit='1'>" \
                            "<FILTER>" \
                                f"<EQ name='Id' value='{camera_id}' />" \
                            "</FILTER>" \
                        "</QUERY>" \
                        "</REQUEST>"
        response = requests.post(url, data=message, headers={"Content-Type": "text/xml"})

        data = response.json()
        
        data = data['RESPONSE']['RESULT'][0]['Camera'][0]
        camera_info.append(data)

    print(camera_info)
    return camera_info