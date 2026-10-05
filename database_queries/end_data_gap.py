from DB_config.DB_init_connection import get_connection
from datetime import datetime, timezone

def end_data_gap(data_gap_id):
    conn = get_connection()
    cur = conn.cursor()
    time = datetime.now(timezone.utc).replace(tzinfo=None)

    cur.execute("UPDATE data_gap " \
                "SET gap_end = %s " \
                "WHERE data_gap_id = %s", (time, data_gap_id,))

    conn.commit()
    cur.close()
    conn.close()