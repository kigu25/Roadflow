from DB_config.DB_init_connection import get_connection

def get_camera_coord_query():
    conn = get_connection()
    
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT camera_id, camera_name, latitude, longitude FROM camera")

    result = cur.fetchall()

    cur.close()
    conn.close()

    for x in result:
        x['latitude'] = float(x['latitude'])
        x['longitude'] = float(x['longitude'])

    return result


def get_camera_data_query(camera_name):

    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM camera WHERE camera_name LIKE %s", (camera_name,))
    result = cur.fetchone()

    cur.close()
    conn.close()

    return result


def get_latest_img_query(camera_name):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT photo.original_filepath " \
    "FROM photo " \
    "INNER JOIN camera ON photo.camera_id = camera.camera_id " \
    "WHERE camera.camera_name = %s " \
    "ORDER BY photo_time DESC " \
    "LIMIT 1", (camera_name,))

    img_filepath = cur.fetchone()
    cur.close()
    conn.close()

    return img_filepath