#!/usr/bin/env python3
"""Create a Flask app"""

from auth import Auth
from flask import Flask, request, jsonify, abort, redirect

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
    # exctract form data
    email = request.form.get("email")
    password = request.form.get("password")

    # check that email and password fields are present
    if not email or not password:
        return jsonify({"message": "Missing email or password"}), 400

    try:
        # register a new user
        new_user = AUTH.register_user(email, password)
        return jsonify({"email": new_user.email,
                        "message": "user created"}), 200
    except ValueError as e:
        # case where the email is already registered
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """login function"""
    email = request.form.get("email")
    password = request.form.get("password")

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": "{}".format(email),
                            "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """logout function"""
    session_id = request.cookies.get("session_id")
    try:
        user = AUTH.get_user_from_session_id(session_id)
        AUTH.destroy_session(user.id)
        return redirect("http://localhost:5000/", 302)
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
