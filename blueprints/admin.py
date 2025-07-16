from flask import Blueprint, request
from utils.auth import auth_required
from utils.api_client import forward_request

admins_bp = Blueprint("admins", __name__)


@admins_bp.route("", methods=["GET"])
@auth_required
def get_admins():
    """Get all admins - authentication required"""
    params = request.args.to_dict()
    return forward_request("/admins", params=params)


@admins_bp.route("/mechanics/<id>", methods=["GET"])
@auth_required
def get_mechanic_by_id(id):
    """Get mechanic by ID - authentication required"""
    return forward_request(f"/mechanics/{id}")


@admins_bp.route("", methods=["POST"])
@auth_required
def create_admin():
    """Create a new admin - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request("/admins", method="POST", json_data=payload)


@admins_bp.route("/mechanics/<id>", methods=["PATCH"])
@auth_required
def update_mechanic(id):
    """Update mechanic by ID - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request(f"/mechanics/{id}", method="PATCH", json_data=payload)


@admins_bp.route("/<id>", methods=["DELETE"])
@auth_required
def delete_admin(id):
    """Delete admin by ID - authentication required"""
    return forward_request(f"/admins/{id}", method="DELETE")
