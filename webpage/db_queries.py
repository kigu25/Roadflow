from DB_config.DB_init_connection import get_connection

#Used in leaf_map to put out cameras on the map
def get_all_camera_data_query():
    conn = get_connection()
    
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT camera_id, camera_name, latitude, longitude, trafikverket_id FROM camera")

    result = cur.fetchall()

    cur.close()
    conn.close()

    for x in result:
        x['latitude'] = float(x['latitude'])
        x['longitude'] = float(x['longitude'])

    return result


def get_avg_detections_per_day(camera_name):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT DATE_FORMAT(photo.photo_time, '%Y-%m-%d') AS photo_day, " \
                        "AVG(analysis.detected_vehicles) AS avg_vehicles " \
                "FROM analysis " \
                "INNER JOIN photo ON analysis.photo_id = photo.photo_id " \
                "INNER JOIN camera ON photo.camera_id = camera.camera_id " \
                "WHERE camera.camera_name = %s " \
                "AND HOUR(photo.photo_time) BETWEEN 6 AND 17 " \
                "GROUP BY photo_day " \
                "ORDER BY photo_day", (camera_name,))

    #Returns all days and it's AVG
    days = cur.fetchall()
    cur.close()
    conn.close()

    if not days:
        return None

    #Take each day's AVG and divide by number of days to get an actuall AVG
    tot_sum = 0
    for x in days:
        tot_sum+=x['avg_vehicles']
    avg_per_day = round(float(tot_sum / len(days)), 2)

    return avg_per_day



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


def get_historical_data_per_hour(camera_name):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT HOUR(photo.photo_time) AS photo_hour, " \
                        "ROUND(AVG(analysis.detected_vehicles) ,1) AS avg_vehicles, " \
                        "MAX(analysis.detected_vehicles) AS max_vehicles " \
                "FROM photo " \
                "INNER JOIN analysis ON analysis.photo_id = photo.photo_id " \
                "INNER JOIN camera ON camera.camera_id = photo.camera_id " \
                "WHERE camera.camera_name = %s " \
                "GROUP BY photo_hour " \
                "ORDER BY photo_hour", (camera_name,))
    res = cur.fetchall()
    cur.close()
    conn.close()
    return res