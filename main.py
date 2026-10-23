import time
from datetime import datetime, timedelta
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


    #--pipeling flag to start image polling
    if args.pipeline:
        from modules.pipelines.img_handling_pipeline import img_handling_pipeline
        fixed_polling_cadence = 180
        print("Starting image-polling from Trafikverket.")

        while True:
            start_iteration_time = datetime.now()
            try:
                img_handling_pipeline()
            except Exception as exc:
                print(f"TIME: {datetime.now()}. Could not complete a full run of the pipeline, retrying after sleep. CODE:{exc}")

            itteration_end = datetime.now()
            tot_iteration_time_sec = (itteration_end - start_iteration_time).total_seconds()
            time_to_sleep = max(0, fixed_polling_cadence - tot_iteration_time_sec)
            print(f"Iteration complete with duration of: {tot_iteration_time_sec} seconds.")
            print(f"Now entering sleep for {time_to_sleep} seconds.")
            time.sleep(time_to_sleep)



    #--webpage flag to run the webpage on localhost
    if args.webpage:
        app = Flask(__name__, template_folder="webpage/templates", static_folder="webpage/static")
        
        app.json.ensure_ascii = False
        
        for bp in blueprints:
            app.register_blueprint(bp)
            
        app.run(host="127.0.0.1", port=5000, debug=True)
    




if __name__ == "__main__":
    main()