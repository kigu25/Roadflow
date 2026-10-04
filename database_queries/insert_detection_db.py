from DB_config.DB_init_connection import get_connection

def insert_detections_db(analysis_id, all_detections):
    conn = get_connection()
    cur = conn.cursor()

    for x in all_detections:
        vehicle_class = x['vehicle']
        confident = x['confident']
        x1 = x['x1']
        y1 = x['y1']
        x2 = x['x2']
        y2 = x['y2']

        cur.execute("INSERT INTO detection(analysis_id, " \
                    "vehicle_class, " \
                    "detection_confidence, " \
                    "bounding_x1, " \
                    "bounding_y1, " \
                    "bounding_x2, " \
                    "bounding_y2) " \
                    
                    "VALUES(%s,%s,%s,%s,%s,%s,%s)", (analysis_id, vehicle_class, confident, x1, y1, x2, y2))

    conn.commit()
    cur.close()
    conn.close()