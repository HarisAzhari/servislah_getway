from functools import wraps
from flask import request, jsonify
from flask_limiter.util import get_remote_address


def get_user_or_ip():
    """Get Bearer token or fall back to IP address for rate limiting"""
    auth_header = request.headers.get("Authorization")

    if auth_header and auth_header.startswith("Bearer "):
        # Use the Bearer token directly as the key (it's unique per user)
        token = auth_header.split(" ")[1]
        return f"token:{token}"

    # Fall back to IP address if no valid Bearer token
    return f"ip:{get_remote_address()}"


def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"error": "Authorization header required"}), 401

        if not auth_header.startswith("Bearer "):
            return (
                jsonify({"error": "Authorization header must start with Bearer"}),
                401,
            )

        return f(*args, **kwargs)

    return decorated_function
