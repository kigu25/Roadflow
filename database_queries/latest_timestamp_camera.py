from DB_config.DB_init_connection import get_connection

def get_latest_timestamp_cam(camera_id):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT photo_time FROM photo WHERE camera_id = %s " \
                    "ORDER BY photo_time DESC LIMIT 1", (camera_id,))

    latest_timestamp = cur.fetchone()
    cur.close()
    conn.close()

    if latest_timestamp == None:
        return None

    return latest_timestamp['photo_time']