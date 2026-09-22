from dotenv import load_dotenv
from DB_config.DB_init_connection import get_connection
from modules.camera_setup.camera_matching import camera_matching
from modules.image_handling.fetch_image import fetch_image



def main():
    load_dotenv()
    conn = get_connection()
    conn.close()

    #Should be loaded once per software-start to ensure that every camera that user wants is loaded and placed in DB as suposed
    #Or when a new camera is added to "selected_cameras.txt"
    #camera_matching()
    

    #Will be an timer/loop here to run the fetch in a fixed cadence
    fetch_image()




if __name__ == "__main__":
    main()