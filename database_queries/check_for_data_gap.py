from DB_config.DB_init_connection import get_connection

def check_for_data_gap(camera_id):
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