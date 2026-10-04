from DB_config.DB_init_connection import get_connection
from modules.utils.camera_id_converter import camera_id_converter


def insert_image_db(camera_id, photo_time, filepath):
    conn = get_connection()
    cur = conn.cursor()

    camera_id = camera_id_converter(camera_id)

    cur.execute("INSERT INTO photo(camera_id, photo_time, original_filepath) "
                "VALUES(%s, %s, %s)", (camera_id, photo_time, filepath))

    conn.commit()

    photo_id = cur.lastrowid

    cur.close()
    conn.close()

    return photo_id