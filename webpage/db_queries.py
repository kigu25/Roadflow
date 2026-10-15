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

    avg_detections_tot = round(float(tot_sum / len(days)), 2)

    return avg_detections_tot


def get_max_detections_camera(camera_name):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT MAX(detected_vehicles) as max_detection_value " \
                "FROM analysis " \
                "INNER JOIN photo ON photo.photo_id = analysis.photo_id " \
                "INNER JOIN camera ON camera.camera_id = photo.camera_id " \
                "WHERE camera_name = %s", (camera_name,))
    max_detected = cur.fetchone()
    cur.close()
    conn.close()
    return max_detected


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


def get_latest_img_for_time_frame(camera_name, end_time):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT photo.original_filepath " \
        "FROM photo " \
        "INNER JOIN camera ON photo.camera_id = camera.camera_id " \
            "WHERE camera.camera_name = %s " \
            "AND photo.photo_time < %s " \
        "ORDER BY photo_time DESC " \
        "LIMIT 1", (camera_name, end_time,))

    img_filepath = cur.fetchone()
    cur.close()
    conn.close()

    return img_filepath


def get_vehicles_per_hour_based_on_date(camera_name, date):
    
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT HOUR(photo.photo_time) AS photo_hour, " \
                        "ROUND(AVG(analysis.detected_vehicles), 2) AS avg_vehicles, " \
                        "COUNT(*) AS nr_photos " \
                "FROM photo " \
                "INNER JOIN analysis ON analysis.photo_id = photo.photo_id " \
                "INNER JOIN camera ON camera.camera_id = photo.camera_id " \
                "WHERE camera_name = %s " \
                "AND DATE(photo.photo_time) = %s " \
                "GROUP BY photo_hour " \
                "ORDER BY photo_hour", (camera_name, date))
    
    hours = cur.fetchall()
    cur.close()
    conn.close()

    #avg from decimal to float
    for x in hours:
        x['avg_vehicles'] = float(x['avg_vehicles'])
        
    return hours


def get_data_heatmap(start_time, end_time):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT camera.camera_id, camera.camera_name, ROUND(AVG(analysis.detected_vehicles), 2) AS avg_vehicles " \
    "FROM camera " \
    "LEFT JOIN photo ON camera.camera_id = photo.camera_id " \
        "AND photo.photo_time >= %s " \
        "AND photo.photo_time < %s " \
    "LEFT JOIN analysis ON analysis.photo_id = photo.photo_id " \
    "GROUP BY camera.camera_id", (start_time, end_time,))


    result = cur.fetchall()
    cur.close()
    conn.close()

    return result


def check_for_data_gap_in_timewindow(camera_id, start_time, end_time):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT camera_id, gap_id, reason FROM data_gap " \
    "WHERE camera_id = %s " \
    "AND gap_start >= %s " \
    "AND gap_end < %s", (camera_id, start_time, end_time,))

    gaps = cur.fetchone()
    cur.close()
    conn.close()

    return gaps