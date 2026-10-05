from DB_config.DB_init_connection import get_connection
from datetime import datetime, timezone

def create_data_gap(camera_id, reason):

    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    

    cur.execute("SELECT data_gap_id FROM data_gap " \
                    "WHERE camera_id = %s AND gap_end IS NULL", (camera_id,))
    open_gap = cur.fetchone()

    if open_gap is None:
        time = datetime.now(timezone.utc).replace(tzinfo=None)
        cur.execute("INSERT INTO data_gap(camera_id, gap_start, reason) " \
                        "VALUES(%s,%s,%s)", (camera_id, time, reason))
        conn.commit()


    cur.close()
    conn.close()