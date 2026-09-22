from DB_config.DB_init_connection import get_connection


def insert_image_db(camera_id, photo_time, filepath):
    conn = get_connection()
    cur = conn.cursor()

    camera_id = int(camera_id.rsplit("_", 1)[-1])
    print(camera_id)
    print(photo_time)

    cur.close()
    conn.close()