from flask import Blueprint, jsonify, request, send_file
from webpage.db_queries import get_all_camera_data_query, get_latest_img_query, get_avg_detections_per_day, get_historical_data_per_hour, get_max_detections_camera

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


@endpoint_route.route("/get/nrdetections/for/camera/timeframe")
def get_nrdetections_for_camera_within_timeframe():
    camera_name = request.args.get("camera_name")
    start_time = request.args.get("start_time")
    end_time = request.args.get("end_time")



@endpoint_route.route("/get/latest/img")
def get_latest_photo():
    camera_name = request.args.get("camera_name")
    img_filepath = get_latest_img_query(camera_name)
    if img_filepath == None:
        return jsonify({"Error": "No image found"}), 404
    return send_file(img_filepath['original_filepath'])


@endpoint_route.route("/historical/data/hour")
def historical_data_hour():
    camera_name = request.args.get("camera_name")
    return jsonify(get_historical_data_per_hour(camera_name))