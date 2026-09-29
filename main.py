import time
from dotenv import load_dotenv
from modules.image_analyzing.image_processing import image_processing
from modules.pipelines.img_handling_pipeline import img_handling_pipeline
from run_setup import run_setup
import argparse
from flask import Flask
from webpage.routes import blueprints


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="RoadFlow")
    parser.add_argument("--setup", action="store_true", help="Use the flag '--setup' if it's the first software start or if a new camera " \
                            "is added in 'selected_cameras.txt'")
    args = parser.parse_args()


    #Test image_processing encaspuled by uncommenting this function-call and enter the filepath for img to be analyzed.
    #image_processing("image_storage/original/SE_STA_CAMERA_0_1075001169/2026-09-27T13-21-00+00-00.jpg", 0.40 , True)


    #if main is called witht he flag --setup this will be ran
    if args.setup:
        run_setup()
        return

    #This function will be the main function being called for fetching new images, using a timer/loop to run at a fixed cadence
    #while True:
        #img_handling_pipeline()
        #time.sleep(200)




    app = Flask(__name__, template_folder="webpage/templates", static_folder="webpage/static")
    for bp in blueprints:
        app.register_blueprint(bp)
    app.run(host="127.0.0.1", port=5000)








if __name__ == "__main__":
    main()