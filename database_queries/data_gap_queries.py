from DB_config.DB_init_connection import get_connection
from datetime import datetime, timezone

def create_gap(camera_id, reason):

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


def end_gap(data_gap_id):
    conn = get_connection()
    cur = conn.cursor()
    time = datetime.now(timezone.utc).replace(tzinfo=None)

    cur.execute("UPDATE data_gap " \
                "SET gap_end = %s " \
                "WHERE data_gap_id = %s", (time, data_gap_id,))

    conn.commit()
    cur.close()
    conn.close()


def check_for_gap(camera_id):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT data_gap_id FROM data_gap " \
                    "WHERE camera_id = %s AND gap_end IS NULL " \
                    "ORDER BY gap_start DESC LIMIT 1", (camera_id,))

    data_gap = cur.fetchone()
    cur.close()
    conn.close()

    if data_gap is None:
        return None
    else:
        data_gap_id = data_gap['data_gap_id']
        return data_gap_id