from dotenv import load_dotenv
from DB_config.DB_init_connection import get_connection
from modules.camera_setup.camera_matching import camera_matching
from modules.image_handling.build_links import build_links

def main():
    load_dotenv()
    conn = get_connection()
    conn.close()

    camera_matching() # Should be loaded once per software-start to ensure that every camera that user wants is loaded and placed in DB as suposed
    build_links()




if __name__ == "__main__":
    main()