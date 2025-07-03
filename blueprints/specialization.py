# blueprints/specialization.py
from flask import Blueprint, request
from utils.auth import auth_required
from utils.api_client import forward_request

specializations_bp = Blueprint("specializations", __name__)


@specializations_bp.route("", methods=["GET"])
@auth_required
def get_specializations():
    """Get specializations with optional query parameters - authentication required"""
    # Get all query parameters and forward them to the external API
    params = request.args.to_dict()
    return forward_request("/specializations", params=params)


@specializations_bp.route("", methods=["POST"])
@auth_required
def create_specialization():
    """Create a new specialization - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request("/specializations", method="POST", json_data=payload)


@specializations_bp.route("/<id>", methods=["GET"])
@auth_required
def get_specialization_by_id(id):
    """Get specialization by ID - authentication required"""
    return forward_request(f"/specializations/{id}")


@specializations_bp.route("/<id>", methods=["PATCH"])
@auth_required
def update_specialization(id):
    """Update specialization by ID - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request(f"/specializations/{id}", method="PATCH", json_data=payload)


@specializations_bp.route("/<id>", methods=["DELETE"])
@auth_required
def delete_specialization(id):
    """Delete specialization by ID - authentication required"""
    return forward_request(f"/specializations/{id}", method="DELETE")
