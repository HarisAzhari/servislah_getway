# blueprints/service.py
from flask import Blueprint, request
from utils.auth import auth_required
from utils.api_client import forward_request

services_bp = Blueprint("services", __name__)


@services_bp.route("", methods=["GET"])
@auth_required
def get_services():
    """Get all services - authentication required"""
    params = request.args.to_dict()
    return forward_request("/services", params=params)


@services_bp.route("/<id>", methods=["GET"])
@auth_required
def get_service_by_id(id):
    """Get service by ID - authentication required"""
    return forward_request(f"/services/{id}")


@services_bp.route("/name/<name>", methods=["GET"])
@auth_required
def get_service_by_name(name):
    """Get service by name - authentication required"""
    return forward_request(f"/services/name/{name}")


@services_bp.route("", methods=["POST"])
@auth_required
def create_service():
    """Create a new service - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request("/services", method="POST", json_data=payload)

@services_bp.route("/<id>", methods=["PATCH"])
@auth_required
def update_service(id):
    """Update service by ID - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request(f"/services/{id}", method="PATCH", json_data=payload)


@services_bp.route("/<id>", methods=["DELETE"])
@auth_required
def delete_service(id):
    """Delete service by ID - authentication required"""
    return forward_request(f"/services/{id}", method="DELETE")
