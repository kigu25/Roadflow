import os

def save_image(image, camera_id, photo_time, image_type="original"):
    photo_time = photo_time.isoformat().replace(":", "-")


   
    folder = f"image_storage/{image_type}/{camera_id}"
   
    os.makedirs(folder, exist_ok=True)

    filepath = f"{folder}/{photo_time}.jpg"

    with open(filepath, "wb") as f:
        f.write(image)

    return filepath