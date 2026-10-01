from flask import Blueprint, jsonify
from webpage.db_queries import get_camera_coord_query

endpoint_route = Blueprint('endpoints', __name__, url_prefix="/endpoints")

@endpoint_route.route("/get/cameras")
def get_cameras():
    return jsonify(get_camera_coord_query())