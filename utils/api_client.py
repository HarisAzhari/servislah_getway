import os
import requests
from flask import request, jsonify

# Default base URL that can be overridden
BASE_URL = "https://servislahserver-production.up.railway.app/api/v1"


def set_base_url(new_url):
    """Set a new base URL for API requests"""
    global BASE_URL
    BASE_URL = new_url
    return BASE_URL


def get_base_url():
    """Get the current base URL"""
    return BASE_URL


def forward_request(endpoint, method="GET", json_data=None, params=None):
    """Generic function to forward requests to external API"""
    auth_header = request.headers.get("Authorization")

    headers = {"Authorization": auth_header}
    if json_data:
        headers["Content-Type"] = "application/json"

    try:
        response = requests.request(
            method=method,
            url=f"{BASE_URL}{endpoint}",
            headers=headers,
            json=json_data,
            params=params,
        )
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to {method.lower()} {endpoint}"}), 500
