# Flask App Guide

This guide provides information on how to declare API routes in a Flask app, manage cookies, retrieve request form data, and return various HTTP status codes.

## Table of Contents

1. [Declaring API Routes](#declaring-api-routes)
2. [Managing Cookies](#managing-cookies)
3. [Retrieving Request Form Data](#retrieving-request-form-data)
4. [Returning HTTP Status Codes](#returning-http-status-codes)

## Declaring API Routes

To declare API routes in a Flask app, use the `@app.route` decorator. Here's an example:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask app!"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"key": "value"}
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def post_data():
    new_data = request.json
    return jsonify(new_data), 201

if __name__ == '__main__':
    app.run(debug=True)
