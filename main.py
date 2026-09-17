from dotenv import load_dotenv
from DB_config.DB_init_connection import get_connection
from modules.trafikverket_api.fetch_image import fetch_image
from modules.trafikverket_api.get_all_cameras import get_all_cameras

def main():
    load_dotenv()
    conn = get_connection()
    conn.close()

    get_all_cameras()





if __name__ == "__main__":
    main()