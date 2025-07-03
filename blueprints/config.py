from flask import Blueprint, request, jsonify
from utils.api_client import get_base_url, set_base_url

config_bp = Blueprint("config", __name__)


@config_bp.route("/base-url", methods=["GET"])
def get_current_base_url():
    """Get the current base URL"""
    return (
        jsonify(
            {
                "base_url": get_base_url(),
                "message": "Current base URL retrieved successfully",
            }
        ),
        200,
    )


@config_bp.route("/base-url", methods=["POST"])
def update_base_url():
    """Update the base URL"""
    try:
        data = request.get_json()

        if not data or "base_url" not in data:
            return jsonify({"error": "Missing 'base_url' in request body"}), 400

        new_url = data["base_url"]

        # Basic URL validation
        if not new_url.startswith(("http://", "https://")):
            return (
                jsonify({"error": "Base URL must start with http:// or https://"}),
                400,
            )

        # Update the base URL
        updated_url = set_base_url(new_url)

        return (
            jsonify(
                {"message": "Base URL updated successfully", "base_url": updated_url}
            ),
            200,
        )

    except Exception as e:
        return jsonify({"error": f"Failed to update base URL: {str(e)}"}), 500


@config_bp.route("/base-url/reset", methods=["POST"])
def reset_base_url():
    """Reset the base URL to default"""
    try:
        default_url = "http://localhost:7878/api/v1"
        updated_url = set_base_url(default_url)

        return (
            jsonify(
                {
                    "message": "Base URL reset to default successfully",
                    "base_url": updated_url,
                }
            ),
            200,
        )

    except Exception as e:
        return jsonify({"error": f"Failed to reset base URL: {str(e)}"}), 500
