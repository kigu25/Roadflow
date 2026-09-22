from DB_config.DB_init_connection import get_connection

def insert_cameras_DB(matched):


    conn = get_connection()
    cur = conn.cursor()

    for x in matched:
        trafikverket_id = x['id']
        camera_id = int(trafikverket_id.rsplit("_", 1)[-1])
        camera_name = x['name']
        coordinates = x['geo'].replace(")", "").split("(")
        coordinates = coordinates[1].split()
        longitude = coordinates[0]
        latitude = coordinates[1]

        cur.execute("INSERT INTO camera(camera_id, trafikverket_id, camera_name, latitude, longitude) "
                "VALUES(%s, %s, %s, %s, %s)", (camera_id, trafikverket_id, camera_name, latitude, longitude))
        
    conn.commit()
    cur.close()
    conn.close()