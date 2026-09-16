import requests
from PIL import Image


def fetch_image():
    link = 'https://api.trafikinfo.trafikverket.se/v2/Images/data/road.infrastructure.camera/TrafficFlowCamera_39638125.jpg?type=fullsize&maxage=140'
    response = requests.get(link)


    with open("image_storage/original/sparad_bild.jpg", "wb") as f:
        f.write(response.content)

    img = Image.open("image_storage/original/sparad_bild.jpg")
    img.show()


    