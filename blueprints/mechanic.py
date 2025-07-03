# blueprints/mechanic.py
from flask import Blueprint, request
from utils.auth import auth_required
from utils.api_client import forward_request

mechanics_bp = Blueprint("mechanics", __name__)


@mechanics_bp.route("", methods=["GET"])
@auth_required
def get_mechanics():
    """Get all mechanics - authentication required"""
    params = request.args.to_dict()
    return forward_request("/mechanics", params=params)


@mechanics_bp.route("", methods=["POST"])
@auth_required
def create_mechanic():
    """Create a new mechanic - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request("/mechanics", method="POST", json_data=payload)


@mechanics_bp.route("/<id>", methods=["GET"])
@auth_required
def get_mechanic_by_id(id):
    """Get mechanic by ID - authentication required"""
    return forward_request(f"/mechanics/{id}")


@mechanics_bp.route("/<id>", methods=["PATCH"])
@auth_required
def update_mechanic(id):
    """Update mechanic by ID - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request(f"/mechanics/{id}", method="PATCH", json_data=payload)


@mechanics_bp.route("/<id>", methods=["DELETE"])
@auth_required
def delete_mechanic(id):
    """Delete mechanic by ID - authentication required"""
    return forward_request(f"/mechanics/{id}", method="DELETE")


@mechanics_bp.route("/specialization", methods=["POST"])
@auth_required
def create_mechanic_specialization():
    """Create mechanic specialization - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request(
        "/mechanics/specialization", method="POST", json_data=payload
    )


@mechanics_bp.route("/specialization", methods=["DELETE"])
@auth_required
def delete_mechanic_specialization():
    """Delete mechanic specialization - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request(
        "/mechanics/specialization", method="DELETE", json_data=payload
    )


@mechanics_bp.route("/assign", methods=["POST"])
@auth_required
def assign_mechanic():
    """Assign mechanic - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request("/mechanics/assign", method="POST", json_data=payload)
