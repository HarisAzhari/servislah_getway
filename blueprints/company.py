# blueprints/company.py
from flask import Blueprint, request
from utils.auth import auth_required
from utils.api_client import forward_request

companies_bp = Blueprint("companies", __name__)


@companies_bp.route("", methods=["GET"])
@auth_required
def get_companies():
    """Get all companies - authentication required"""
    params = request.args.to_dict()
    return forward_request("/companies", params=params)


@companies_bp.route("/<id>", methods=["GET"])
@auth_required
def get_companies_by_id(id):
    return forward_request(f"/companies/{id}")


@companies_bp.route("/service-center/<id>", methods=["GET"])
@auth_required
def get_company_service_center(id):
    """Get company service center by ID - authentication required"""
    return forward_request(f"/companies/service-center/{id}")


@companies_bp.route("", methods=["POST"])
@auth_required
def create_company():
    """Create a new company - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request("/companies", method="POST", json_data=payload)


@companies_bp.route("/<id>", methods=["DELETE"])
@auth_required
def delete_company(id):
    """Delete company by ID - authentication required"""
    return forward_request(f"/companies/{id}", method="DELETE")


@companies_bp.route("/<id>", methods=["PATCH"])
@auth_required
def update_company(id):
    """Update company by ID - authentication required"""
    payload = request.get_json()
    if not payload:
        return {"error": "JSON payload required"}, 400
    return forward_request(f"/companies/{id}", method="PATCH", json_data=payload)
