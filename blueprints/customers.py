# blueprints/customers.py
from flask import Blueprint, request
from utils.auth import auth_required
from utils.api_client import forward_request

customers_bp = Blueprint("customers", __name__)


@customers_bp.route("", methods=["GET"])
@auth_required
def get_customers():
    """Get all customers with optional query parameters - authentication required"""
    # Get all query parameters and forward them to the external API
    params = request.args.to_dict()
    return forward_request("/customers", params=params)


@customers_bp.route("/<id>", methods=["GET"])
@auth_required
def get_customer_by_id(id):
    """Get customer by ID - authentication required"""
    return forward_request(f"/customers/{id}")


@customers_bp.route("", methods=["POST"])
@auth_required
def create_customer():
    """Create a new customer - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request("/customers", method="POST", json_data=payload)


@customers_bp.route("/<id>", methods=["PATCH"])
@auth_required
def update_customer(id):
    """Update customer by ID - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request(f"/customers/{id}", method="PATCH", json_data=payload)


@customers_bp.route("/<id>", methods=["DELETE"])
@auth_required
def delete_customer(id):
    """Delete customer by ID - authentication required"""
    return forward_request(f"/customers/{id}", method="DELETE")
