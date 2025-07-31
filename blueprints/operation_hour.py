# blueprints/operation_hour.py
from flask import Blueprint, request
from utils.auth import auth_required
from utils.api_client import forward_request

operation_hours_bp = Blueprint("operation_hours", __name__)


@operation_hours_bp.route("", methods=["POST"])
@auth_required
def create_operation_hour():
    """Create a new operating hour - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request("/operating-hours", method="POST", json_data=payload)


@operation_hours_bp.route("", methods=["GET"])
@auth_required
def get_operation_hours():
    """Get all operating hours with optional query parameters - authentication required"""
    # Get all query parameters and forward them to the external API
    params = request.args.to_dict()
    return forward_request("/operating-hours", params=params)


@operation_hours_bp.route("/<id>", methods=["GET"])
@auth_required
def get_operation_hour_by_id(id):
    """Get operating hour by ID - authentication required"""
    return forward_request(f"/operating-hours/{id}")


@operation_hours_bp.route("/<id>", methods=["PATCH"])
@auth_required
def update_operation_hour(id):
    """Update operating hour by ID - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request(f"/operating-hours/{id}", method="PATCH", json_data=payload)


@operation_hours_bp.route("/<id>", methods=["DELETE"])
@auth_required
def delete_operation_hour(id):
    """Delete operating hour by ID - authentication required"""
    return forward_request(f"/operating-hours/{id}", method="DELETE")
