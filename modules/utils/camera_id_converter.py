def camera_id_converter(trafikverket_id):
    camera_id = int(trafikverket_id.rsplit("_", 1)[-1])
    return camera_id