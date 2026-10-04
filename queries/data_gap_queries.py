from DB_config.DB_init_connection import get_connection
from datetime import datetime, timezone
from modules.utils.camera_id_converter import camera_id_converter

def insert_data_gap(camera_id, reason):
    converted_camera_id = camera_id_converter(camera_id)

    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    

    cur.execute("SELECT data_gap_id FROM data_gap " \
                    "WHERE camera_id = %s AND gap_end IS NULL", (converted_camera_id,))
    open_gap = cur.fetchone()

    if open_gap is None:
        time = datetime.now(timezone.utc).replace(tzinfo=None)
        cur.execute("INSERT INTO data_gap(camera_id, gap_start, reason) " \
                        "VALUES(%s,%s,%s)", (converted_camera_id, time, reason))
        conn.commit()


    cur.close()
    conn.close()