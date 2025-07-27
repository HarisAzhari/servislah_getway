# blueprints/service_center.py
from flask import Blueprint, request
from utils.auth import auth_required
from utils.api_client import forward_request

service_centers_bp = Blueprint("service_centers", __name__)


@service_centers_bp.route("", methods=["GET"])
@auth_required
def get_service_centers():
    # Get all query parameters and forward them to the external API
    params = request.args.to_dict()
    return forward_request("/service-centers", params=params)


@service_centers_bp.route("/<id>", methods=["GET"])
@auth_required
def get_service_center_by_id(id):
    """Get service center by ID - authentication required"""
    return forward_request(f"/service-centers/{id}")


@service_centers_bp.route("/name/<name>", methods=["GET"])
@auth_required
def get_service_center_by_name(name):
    """Get service center by name - authentication required"""
    return forward_request(f"/service-centers/name/{name}")


@service_centers_bp.route("", methods=["POST"])
@auth_required
def create_service_center():
    """Create a new service center - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request("/service-centers", method="POST", json_data=payload)


@service_centers_bp.route("/<id>", methods=["DELETE"])
@auth_required
def delete_service_center(id):
    """Delete service center by ID - authentication required"""
    return forward_request(f"/service-centers/{id}", method="DELETE")


@service_centers_bp.route("/<id>", methods=["PATCH"])
@auth_required
def update_service_center(id):
    """Update service center by ID - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request(f"/service-centers/{id}", method="PATCH", json_data=payload)


@service_centers_bp.route("/<id>/operating-hours", methods=["POST"])
@auth_required
def create_service_center_operating_hours(id):
    """Create operating hours for a specific service center - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request(
        f"/service-centers/{id}/operating-hours", method="POST", json_data=payload
    )


@service_centers_bp.route("/<id>/operating-hours", methods=["GET"])
@auth_required
def get_service_center_operating_hours(id):
    """Get operating hours for a specific service center with optional filtering - authentication required"""
    params = request.args.to_dict()
    return forward_request(f"/service-centers/{id}/operating-hours", params=params)


@service_centers_bp.route(
    "/<service_center_id>/operating-hours/<operating_hours_id>", methods=["GET"]
)
@auth_required
def get_service_center_operating_hour_by_id(service_center_id, operating_hours_id):
    """Get specific operating hour by ID for a service center - authentication required"""
    return forward_request(
        f"/service-centers/{service_center_id}/operating-hours/{operating_hours_id}"
    )


@service_centers_bp.route(
    "/<service_center_id>/operating-hours/<operating_hours_id>", methods=["PATCH"]
)
@auth_required
def update_service_center_operating_hours(service_center_id, operating_hours_id):
    """Update operating hours for a specific service center - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request(
        f"/service-centers/{service_center_id}/operating-hours/{operating_hours_id}",
        method="PATCH",
        json_data=payload,
    )


@service_centers_bp.route(
    "/<service_center_id>/operating-hours/<operating_hours_id>", methods=["DELETE"]
)
@auth_required
def delete_service_center_operating_hours(service_center_id, operating_hours_id):
    """Delete specific operating hour by ID for a service center - authentication required"""
    return forward_request(
        f"/service-centers/{service_center_id}/operating-hours/{operating_hours_id}",
        method="DELETE",
    )
