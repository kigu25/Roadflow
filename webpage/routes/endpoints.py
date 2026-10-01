from flask import Blueprint, jsonify, request
from webpage.db_queries import get_camera_coord_query, get_camera_data_query

endpoint_route = Blueprint('endpoints', __name__, url_prefix="/endpoints")

@endpoint_route.route("/get/camera/coords")
def get_camera_coords():
    return jsonify(get_camera_coord_query())


@endpoint_route.route("/get/camera/details")
def get_camera_data():
    camera_name = request.args.get("camera_name")
    return jsonify(get_camera_data_query(camera_name))