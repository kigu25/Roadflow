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
    parser.add_argument("--pipeline", action="store_true", help="Use this '--pipeline' flag for continious image-pipeline usage")
    args = parser.parse_args()


    #To test image_processing encaspuled, uncomment thefunction-call below and enter the filepath for img you want to be analyzed.
    #image_processing("image_storage/original/SE_STA_CAMERA_0_1075001169/2026-09-27T13-21-00+00-00.jpg", 0.40 , True)


    #if main is called with the flag --setup, the setup will be ran. ONLY do this before first start or if a new camera is added in 'selected_cameras.txt'
    if args.setup:
        run_setup()
        return

    #If main is called with the flag --pipeline, the image gathering will run on infinite.
    if args.pipeline:
        while True:
            img_handling_pipeline()
            time.sleep(200)
        return




    app = Flask(__name__, template_folder="webpage/templates", static_folder="webpage/static")

    app.json.ensure_ascii = False
    
    for bp in blueprints:
        app.register_blueprint(bp)
        
    app.run(host="127.0.0.1", port=5000, debug=True)








if __name__ == "__main__":
    main()