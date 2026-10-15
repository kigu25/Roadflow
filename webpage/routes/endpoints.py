from flask import Blueprint, jsonify, request, send_file
from webpage.db_queries import get_all_camera_data_query, get_latest_img_query, get_avg_detections_per_day, get_historical_data_per_hour
from webpage.db_queries import get_max_detections_camera, get_vehicles_per_hour_based_on_date, get_data_heatmap, get_latest_img_for_time_frame
from datetime import datetime, timedelta
endpoint_route = Blueprint('endpoints', __name__, url_prefix="/endpoints")

@endpoint_route.route("/get/all/camera/data")
def get_all_camera_data():
    return jsonify(get_all_camera_data_query())


@endpoint_route.route("/get/avg/detections/day")
def get_camera_stats():
    camera_name = request.args.get("camera_name")
    avg_detections = get_avg_detections_per_day(camera_name)
    return jsonify({"avg_detections_day": avg_detections})


@endpoint_route.route("/get/maxdetections/camera")
def get_max_detections():
    camera_name = request.args.get("camera_name")
    response = get_max_detections_camera(camera_name)
    return jsonify(response)


@endpoint_route.route("/get/detections/for/graph/date")
def get_detected_per_hour_date():
    camera_name = request.args.get("camera_name")
    date = request.args.get("date")
    resp = get_vehicles_per_hour_based_on_date(camera_name, date)
    return jsonify(resp)


@endpoint_route.route("/get/latest/img")
def get_latest_photo():
    camera_name = request.args.get("camera_name")
    img_filepath = get_latest_img_query(camera_name)
    if img_filepath == None:
        return jsonify({"Error": "No image found"}), 404
    return send_file(img_filepath['original_filepath'])


@endpoint_route.route("/get/latest/imge/timeframe")
def get_latest_photo_timeframe():
    camera_name = request.args.get("camera_name")
    date_object = request.args.get("date_object")

    formated_date_time = datetime.fromisoformat(date_object)
    start_time = formated_date_time.replace(tzinfo=None)
    end_time = start_time + timedelta(minutes=15)

    img_filepath = get_latest_img_for_time_frame(camera_name, end_time)
    if img_filepath == None:
        return jsonify({"Error": "No image found"}), 404
    return send_file(img_filepath['original_filepath'])


@endpoint_route.route("/historical/data/hour")
def historical_data_hour():
    camera_name = request.args.get("camera_name")
    return jsonify(get_historical_data_per_hour(camera_name))


@endpoint_route.route("/get/intensity/heatmap/time/date")
def get_intensity_for_heatmap():
    date_object = request.args.get("date_object")

    formated_date_time = datetime.fromisoformat(date_object)

    start_time = formated_date_time.replace(tzinfo=None)
    end_time = start_time + timedelta(minutes=15)

    return jsonify(get_data_heatmap(start_time, end_time))