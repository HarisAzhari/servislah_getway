# blueprints/service_bay.py
from flask import Blueprint, request
from utils.auth import auth_required
from utils.api_client import forward_request

service_bays_bp = Blueprint("service_bays", __name__)


@service_bays_bp.route("", methods=["GET"])
@auth_required
def get_service_bays():
    """Get service bays with optional query parameters - authentication required"""
    # Get all query parameters and forward them to the external API
    params = request.args.to_dict()
    return forward_request("/service-bays", params=params)


@service_bays_bp.route("", methods=["POST"])
@auth_required
def create_service_bay():
    """Create a new service bay - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request("/service-bays", method="POST", json_data=payload)


@service_bays_bp.route("/<id>", methods=["GET"])
@auth_required
def get_service_bay_by_id(id):
    """Get service bay by ID - authentication required"""
    return forward_request(f"/service-bays/{id}")


@service_bays_bp.route("/<id>", methods=["PATCH"])
@auth_required
def update_service_bay(id):
    """Update service bay by ID - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request(f"/service-bays/{id}", method="PATCH", json_data=payload)


@service_bays_bp.route("/<id>", methods=["DELETE"])
@auth_required
def delete_service_bay(id):
    """Delete service bay by ID - authentication required"""
    return forward_request(f"/service-bays/{id}", method="DELETE")


@service_bays_bp.route("/assign", methods=["POST"])
@auth_required
def assign_service_bay():
    """Assign service bay - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request("/service-bays/assign", method="POST", json_data=payload)
