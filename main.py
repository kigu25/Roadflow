import time
from dotenv import load_dotenv
from modules.camera_setup.camera_matching import camera_matching
from modules.image_handling.fetch_image import fetch_image
from modules.image_analyzing.image_processing import image_processing
from modules.pipelines.img_handling_pipeline import img_handling_pipeline



def main():
    load_dotenv()

    #Should be loaded once per software-start to ensure that every camera in "selected_cameras" is loaded and placed in DB as suposed
    #camera_matching()

    #Test image_processing encaspuled.
    #image_processing("image_storage/original/SE_STA_CAMERA_0_1075001082/2026-09-24T10-43-00+00-00.jpg", 0.40 , True)

    #This function will be the main function being called for fetching new images, using a timer/loop to run at a fixed cadence
    while True:
        img_handling_pipeline()
        time.sleep(65)



if __name__ == "__main__":
    main()