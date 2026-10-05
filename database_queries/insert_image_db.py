from DB_config.DB_init_connection import get_connection


def insert_image_db(camera_id, photo_time, filepath):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO photo(camera_id, photo_time, original_filepath) "
                "VALUES(%s, %s, %s)", (camera_id, photo_time, filepath))

    conn.commit()

    photo_id = cur.lastrowid

    cur.close()
    conn.close()

    return photo_id