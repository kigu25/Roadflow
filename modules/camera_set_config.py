def build_set():
    with open("camera_configs/selected_cameras.txt", "r", encoding="utf-8") as x:
        filter_camera_names = set()
        for line in x:
            filter_camera_names.add(line.strip())
    return filter_camera_names