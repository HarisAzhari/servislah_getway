# blueprints/permission.py
from flask import Blueprint, request
from utils.auth import auth_required
from utils.api_client import forward_request

permissions_bp = Blueprint("permissions", __name__)


@permissions_bp.route("", methods=["GET"])
@auth_required
def get_permissions():
    """Get permissions with optional query parameters - authentication required"""
    # Get all query parameters and forward them to the external API
    params = request.args.to_dict()
    return forward_request("/permissions", params=params)


@permissions_bp.route("", methods=["POST"])
@auth_required
def create_permission():
    """Create a new permission - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request("/permissions", method="POST", json_data=payload)


@permissions_bp.route("", methods=["PATCH"])
@auth_required
def update_permission():
    """Update permission - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request("/permissions", method="PATCH", json_data=payload)


@permissions_bp.route("/<id>", methods=["GET"])
@auth_required
def get_permission_by_id(id):
    """Get permission by ID - authentication required"""
    return forward_request(f"/permissions/{id}")


@permissions_bp.route("/<id>", methods=["DELETE"])
@auth_required
def delete_permission(id):
    """Delete permission by ID - authentication required"""
    return forward_request(f"/permissions/{id}", method="DELETE")
