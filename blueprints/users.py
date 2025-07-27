from flask import Blueprint, request
from utils.api_client import forward_request

users_bp = Blueprint("users", __name__)

#Get All Users
@users_bp.route("", methods=["GET"])
def get_users():
    """Get all users - no authentication required"""
    return forward_request("/users")


@users_bp.route("", methods=["POST"])
def create_user():
    """Create a new user - no authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request("/users", method="POST", json_data=payload)


@users_bp.route("/<id>", methods=["GET"])
def get_user_by_id(id):
    """Get user by ID - no authentication required"""
    return forward_request(f"/users/{id}")


@users_bp.route("/<id>", methods=["PATCH"])
def update_user(id):
    """Update user by ID - no authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request(f"/users/{id}", method="PATCH", json_data=payload)


@users_bp.route("/<id>", methods=["DELETE"])
def delete_user(id):
    """Delete user by ID - no authentication required"""
    return forward_request(f"/users/{id}", method="DELETE")


@users_bp.route("/email/<email>", methods=["GET"])
def get_user_by_email(email):
    """Get user by email - no authentication required"""
    return forward_request(f"/users/email/{email}")
