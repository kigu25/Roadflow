import time
from dotenv import load_dotenv

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
    parser.add_argument("--webpage", action="store_true", help="Use this flag to run the interactive webpage")
    args = parser.parse_args()


    #if main is called with the flag --setup, the setup will be ran. ONLY do this before first start or if a new camera is added in 'selected_cameras.txt'
    if args.setup:
        run_setup()
        print("Successful setup")
        return

    #If main is called with the flag --pipeline, the image gathering will run on infinite.
    if args.pipeline:
        from modules.pipelines.img_handling_pipeline import img_handling_pipeline
        while True:
            img_handling_pipeline()
            time.sleep(200)
        return



    if args.webpage:
        app = Flask(__name__, template_folder="webpage/templates", static_folder="webpage/static")
        
        app.json.ensure_ascii = False
        
        for bp in blueprints:
            app.register_blueprint(bp)
            
        app.run(host="127.0.0.1", port=5000, debug=True)
    








if __name__ == "__main__":
    main()