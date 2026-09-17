from dotenv import load_dotenv
from DB_config.DB_init_connection import get_connection
from modules.trafikverket_api_calls.trafikverket_get_image import fetch_image
from modules.trafikverket_api_calls.get_all_cameras import search_cameras_near

def main():
    load_dotenv()
    conn = get_connection()
    conn.close()

    search_cameras_near()





if __name__ == "__main__":
    main()