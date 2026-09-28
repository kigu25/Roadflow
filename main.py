import time
from dotenv import load_dotenv
from modules.image_handling.fetch_image import fetch_image
from modules.image_analyzing.image_processing import image_processing
from modules.pipelines.img_handling_pipeline import img_handling_pipeline
from run_setup import run_software_setup
import argparse


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="RoadFlow")
    parser.add_argument("--setup", action="store_true", help="Use the flagg '--setup' if it's the fist software start or if a new camera " \
                            "is added in 'selected_cameras.txt'")
    args = parser.parse_args()



    #Test image_processing encaspuled by entering filepath and uncomment the function.
    #image_processing("image_storage/original/SE_STA_CAMERA_0_1075001169/2026-09-27T13-21-00+00-00.jpg", 0.40 , True)


    #run_software_setup()

    #if main is called witht he flag --setup this will be ran
    if args.setup():
        run_software_setup()
        return


    #This function will be the main function being called for fetching new images, using a timer/loop to run at a fixed cadence
    while True:
        img_handling_pipeline()
        time.sleep(65)



if __name__ == "__main__":
    main()