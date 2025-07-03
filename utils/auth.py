from functools import wraps
from flask import request, jsonify

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
