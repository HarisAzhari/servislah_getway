# blueprints/review.py
from flask import Blueprint, request
from utils.auth import auth_required
from utils.api_client import forward_request

reviews_bp = Blueprint("reviews", __name__)


@reviews_bp.route("", methods=["GET"])
@auth_required
def get_reviews():
    """Get reviews with optional query parameters - authentication required"""
    # Get all query parameters and forward them to the external API
    params = request.args.to_dict()
    return forward_request("/reviews", params=params)


@reviews_bp.route("", methods=["POST"])
@auth_required
def create_review():
    """Create a new review - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request("/reviews", method="POST", json_data=payload)


@reviews_bp.route("/<id>", methods=["GET"])
@auth_required
def get_review_by_id(id):
    """Get review by ID - authentication required"""
    return forward_request(f"/reviews/{id}")


@reviews_bp.route("/<id>", methods=["PATCH"])
@auth_required
def update_review(id):
    """Update review by ID - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request(f"/reviews/{id}", method="PATCH", json_data=payload)


@reviews_bp.route("/<id>", methods=["DELETE"])
@auth_required
def delete_review(id):
    """Delete review by ID - authentication required"""
    return forward_request(f"/reviews/{id}", method="DELETE")
