import requests
import os

def search_cameras_near():

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


    with open("all_cameras.txt", "w", encoding="utf-8") as f:
        for camera in data:
            camera_id = camera['Id']
            name = camera['Name']
            desc = camera['Status']

            f.write(camera_id)
            f.write(' ')
            f.write(name)
            f.write('\n')
            f.write('\n')
            f.write('\n')


