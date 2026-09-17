import requests
import os
from modules.camera_set_config import build_set

def get_all_cameras():

    url = "https://api.trafikinfo.trafikverket.se/v2/data.json"

    api_key = os.getenv("trafikverket_api_key")

    
    message = "<REQUEST>" \
                f"<LOGIN authenticationkey='{api_key}'/>" \
                "<QUERY objecttype='Camera' namespace='road.infrastructure' schemaversion='1.1' limit='2000'>" \
                    "<FILTER>" \
                        "<EQ name='Type' value='Trafikflödeskamera' />" \
                    "</FILTER>" \
                "</QUERY>" \
                "</REQUEST>"


    response = requests.post(url, data=message, headers={"Content-Type": "text/xml"})

    data = response.json()

    data = data['RESPONSE']['RESULT'][0]['Camera']


    with open("camera_configs/all_cameras.txt", "w", encoding="utf-8") as f:
        for camera in data:
            camera_id = camera['Id']
            name = camera['Name']

            camera_set = build_set()

            if name in camera_set:
                print("SUCCESS" + " " + name)

            f.write(camera_id)
            f.write(' ')
            f.write(name)
            f.write('\n')
            f.write('\n')
            f.write('\n')


