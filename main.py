from dotenv import load_dotenv
from modules.camera_setup.camera_matching import camera_matching
from modules.image_handling.fetch_image import fetch_image
from modules.image_analyzing.image_processing import image_processing
from modules.pipelines.img_handling_pipeline import img_handling_pipeline



def main():
    load_dotenv()


    #Should be loaded once per software-start to ensure that every camera in "selected_cameras" is loaded and placed in DB as suposed
    #camera_matching()
    

  
   


    #Used to run an image through the AI witohut saving to DB
    #image_processing("image_storage/analyzed/SE_STA_CAMERA_Orion_2500033/2026-09-23T15-24-00+00-00.jpg", 1, 2, 3, False)

    #This function will be the main function being called for fetching new images, using a timer/loop to run at a fixed cadence
    img_handling_pipeline()



if __name__ == "__main__":
    main()