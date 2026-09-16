from dotenv import load_dotenv
from DB_config.DB_init_connection import get_connection




def main():
    load_dotenv()
    conn = get_connection()
    print(conn)






if __name__ == "__main__":
    main()