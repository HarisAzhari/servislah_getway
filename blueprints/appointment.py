# blueprints/appointment.py
from flask import Blueprint, request
from utils.auth import auth_required
from utils.api_client import forward_request

appointments_bp = Blueprint("appointments", __name__)


@appointments_bp.route("", methods=["GET"])
@auth_required
def get_appointments():
    """Get appointments with optional query parameters - authentication required"""
    # Get all query parameters and forward them to the external API
    params = request.args.to_dict()
    print("Params:", params)
    return forward_request("/appointments", params=params)


@appointments_bp.route("/nearest", methods=["GET"])
@auth_required
def get_nearest_appointments():
    """Get nearest appointments with optional query parameters - authentication required"""
    # Get all query parameters and forward them to the external API
    params = request.args.to_dict()
    return forward_request("/appointments/nearest", params=params)


@appointments_bp.route("/<id>", methods=["GET"])
@auth_required
def get_appointment_by_id(id):
    """Get appointment by ID - authentication required"""
    return forward_request(f"/appointments/{id}")


@appointments_bp.route("/name/<name>", methods=["GET"])
@auth_required
def get_appointment_by_name(name):
    """Get appointment by name - authentication required"""
    return forward_request(f"/appointments/name/{name}")


@appointments_bp.route("", methods=["POST"])
@auth_required
def create_appointment():
    """Create a new appointment - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request("/appointments", method="POST", json_data=payload)


@appointments_bp.route("/<id>", methods=["PATCH"])
@auth_required
def update_appointment(id):
    """Update appointment by ID - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request(f"/appointments/{id}", method="PATCH", json_data=payload)


@appointments_bp.route("/<id>", methods=["DELETE"])
@auth_required
def delete_appointment(id):
    """Delete appointment by ID - authentication required"""
    return forward_request(f"/appointments/{id}", method="DELETE")
