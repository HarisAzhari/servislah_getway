import os
import requests
from flask import request, jsonify

BASE_URL = os.getenv("BASE_URL")


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
