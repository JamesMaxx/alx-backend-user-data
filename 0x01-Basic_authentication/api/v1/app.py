#!/usr/bin/env python3
"""
Route module for the API

This module is the main entry point for the API. It sets up the Flask app and
configures the CORS settings. It also imports the appropriate authentication
module based on the `AUTH_TYPE` environment variable. It defines error handlers
for the 404, 401, and 403 errors. It also defines a before request handler to
validate the requests.
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
AUTH_TYPE = getenv("AUTH_TYPE")

if AUTH_TYPE == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()
elif AUTH_TYPE == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """
    Not found handler

    This function handles the 404 error by returning a JSON response with an
    error message.

    Args:
        error: The error object.

    Returns:
        A JSON response with a 404 status code and an error message.
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized_error(error) -> str:
    """
    Unauthorized handler

    This function handles the 401 error by returning a JSON response with an
    error message.

    Args:
        error: The error object.

    Returns:
        A JSON response with a 401 status code and an error message.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_error(error) -> str:
    """
    Forbidden handler

    This function handles the 403 error by returning a JSON response with an
    error message.

    Args:
        error: The error object.

    Returns:
        A JSON response with a 403 status code and an error message.
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request() -> str:
    """
    Before Request Handler

    This function validates the requests. It checks if the `auth` object is
    None and returns early if it is. It defines a list of excluded paths and
    checks if the request path is in the list. If it is not, it calls the
    `require_auth` method of the `auth` object. If the authorization header is
    None, it aborts with a 401 status code. If the current user is None, it
    aborts with a 403 status code.

    Args:
        None

    Returns:
        None
    """
    if auth is None:
        return

    excluded_paths = ['/api/v1/status/',
                      '/api/v1/unauthorized/',
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
