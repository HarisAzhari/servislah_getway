# blueprints/customer_groups.py
from flask import Blueprint, request
from utils.auth import auth_required
from utils.api_client import forward_request

customer_groups_bp = Blueprint("customer_groups", __name__)


@customer_groups_bp.route("", methods=["GET"])
@auth_required
def get_customer_groups():
    """Get all customer groups with optional query parameters - authentication required"""
    # Get all query parameters and forward them to the external API
    params = request.args.to_dict()
    return forward_request("/customer-groups", params=params)


@customer_groups_bp.route("/<id>", methods=["GET"])
@auth_required
def get_customer_group_by_id(id):
    """Get customer group by ID - authentication required"""
    return forward_request(f"/customer-groups/{id}")


@customer_groups_bp.route("", methods=["POST"])
@auth_required
def create_customer_group():
    """Create a new customer group - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request("/customer-groups", method="POST", json_data=payload)


@customer_groups_bp.route("/<id>", methods=["PATCH"])
@auth_required
def update_customer_group(id):
    """Update customer group by ID - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request(f"/customer-groups/{id}", method="PATCH", json_data=payload)


@customer_groups_bp.route("/<id>", methods=["DELETE"])
@auth_required
def delete_customer_group(id):
    """Delete customer group by ID - authentication required"""
    return forward_request(f"/customer-groups/{id}", method="DELETE")
