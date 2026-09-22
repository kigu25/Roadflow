from DB_config.DB_init_connection import get_connection

def insert_image_db():
    conn = get_connection()
    cur = conn.cursor()




    cur.close()
    conn.close()