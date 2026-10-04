from DB_config.DB_init_connection import get_connection


def insert_analysis_db(photo_id, nr_vehicles, filepath):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO analysis(photo_id, detected_vehicles, analyzed_filepath) " \
                "VALUES(%s, %s, %s)", (photo_id, nr_vehicles, filepath))

    conn.commit()

    analysis_id = cur.lastrowid

    cur.close()
    conn.close()

    return analysis_id