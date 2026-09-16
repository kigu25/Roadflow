from dotenv import load_dotenv
from DB_config.DB_init_connection import get_connection
from modules.trafikverket_get_image import fetch_image


def main():
    load_dotenv()
    conn = get_connection()
    conn.close()

    fetch_image()




if __name__ == "__main__":
    main()