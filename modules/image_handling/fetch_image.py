import requests



def fetch_image(camera):

    #Fallback if fullsize does not exist for that specific camera
    if camera.get("PhotoUrlFullsize"):
        photo_link = camera['PhotoUrlFullsize']
    else:
        photo_link = camera['PhotoUrl']

    fetched_img = requests.get(photo_link).content


    return fetched_img