#!/usr/bin/env python3
"""
Route module for the API
"""

from os import getenv
from flask import Flask, jsonify, abort, request
from flask_cors import CORS, cross_origin

from api.v1.views import app_views
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


def get_auth_type() -> str:
    """
    Get the type of authentication from the environment variable.

    Returns:
      - The type of authentication.
    """
    return getenv("AUTH_TYPE")


def create_auth() -> Auth:
    """
    Create an instance of the authentication class based on the authentication type.

    Returns:
      - An instance of the authentication class.
    """
    auth_type = get_auth_type()
    if auth_type == "auth":
        return Auth()
    elif auth_type == "basic_auth":
        return BasicAuth()
    else:
        return None


auth = create_auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """
    Not found handler

    Returns:
      - A JSON response with an error message.
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized_error(error) -> str:
    """
    Unauthorized handler

    Returns:
      - A JSON response with an error message.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_error(error) -> str:
    """
    Forbidden handler

    Returns:
      - A JSON response with an error message.
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request() -> str:
    """
    Before Request Handler
    Requests Validation

    Returns:
      - None if the authentication is not required for the request.
    """
    if auth is None:
        return

    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                      '/api/v1/forbidden/']

    if not auth.require_auth(request.path, excluded_paths):
        return

    if auth.authorization_header(request) is None:
        abort(401)

    if auth.current_user(request) is None:
        abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
