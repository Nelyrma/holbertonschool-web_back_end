#!/usr/bin/env python3
"""Create a Flask app"""

from auth import Auth
from flask import Flask, request, jsonify

AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    """return a JSON payload
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=["POST"])
def users():
    """implement the POST /users route
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        return jsonify({"message": "Missing email or password"}), 400

    try:
        new_user = AUTH.register_user(email, password)
        return jsonify({"email": new_user.email,
                        "message": "user created"}), 200
    except ValueError as e:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
