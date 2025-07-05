# blueprints/vehicles.py
from flask import Blueprint, request
from utils.auth import auth_required
from utils.api_client import forward_request

vehicles_bp = Blueprint("vehicles", __name__)


@vehicles_bp.route("", methods=["GET"])
@auth_required
def get_vehicles():
    return forward_request("/vehicles")


@vehicles_bp.route("", methods=["POST"])
@auth_required
def create_vehicle():
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request("/vehicles", method="POST", json_data=payload)


@vehicles_bp.route("/appointments", methods=["GET"])
@auth_required
def get_vehicle_appointments():
    return forward_request("/vehicles/appointments", params=request.args.to_dict())


@vehicles_bp.route("/user/<user_id>", methods=["GET"])
@auth_required
def get_vehicles_by_user(user_id):
    return forward_request(f"/vehicles/user/{user_id}")


@vehicles_bp.route("/<id>", methods=["GET"])
@auth_required
def get_vehicle_by_id(id):
    return forward_request(f"/vehicles/{id}")


@vehicles_bp.route("/<id>", methods=["PATCH"])
@auth_required
def update_vehicle(id):
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request(f"/vehicles/{id}", method="PATCH", json_data=payload)


@vehicles_bp.route("/<id>", methods=["DELETE"])
@auth_required
def delete_vehicle(id):
    return forward_request(f"/vehicles/{id}", method="DELETE")
