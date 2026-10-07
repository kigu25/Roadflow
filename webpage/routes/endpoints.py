from flask import Blueprint, jsonify, request, send_file
from webpage.db_queries import get_camera_coord_query, get_camera_data_query, get_latest_img_query, get_avg_detections_per_day, get_historical_data_per_hour

endpoint_route = Blueprint('endpoints', __name__, url_prefix="/endpoints")

@endpoint_route.route("/get/camera/coords")
def get_camera_coords():
    return jsonify(get_camera_coord_query())


@endpoint_route.route("/get/camera/details")
def get_camera_data():
    camera_name = request.args.get("camera_name")
    return jsonify(get_camera_data_query(camera_name))


@endpoint_route.route("/get/camera/stats")
def get_camera_stats():
    camera_name = request.args.get("camera_name")
    avg = get_avg_detections_per_day(camera_name)
    return jsonify({"avg_per_day": avg})


@endpoint_route.route("/get/latest/img")
def get_latest_photo():
    camera_name = request.args.get("camera_name")
    img_filepath = get_latest_img_query(camera_name)
    return send_file(img_filepath['original_filepath'])


@endpoint_route.route("/historical/data/hour")
def historical_data_hour():
    camera_name = request.args.get("camera_name")
    return get_historical_data_per_hour(camera_name)