from app import app, db, bcrypt
from app.models import User, encode_auth_token, decode_auth_token

from flask.blueprints import Blueprint
from flask import request, jsonify


@app.route("/", methods=["GET"])
def home():
    data = request.get_json()
    if 'token' not in data.keys():
        return jsonify({"type": "error", "message": "Please log in"}), 401
    else:
        if not decode_auth_token(request.json['token'])[0]:
            return jsonify({"type": "error", "message": "Please log in again"}), 401
    return jsonify({"type": "success", "message": "Logged in"}), 200


auth = Blueprint("auth", "auth", url_prefix="/auth")


@auth.route("/login", methods=["POST"])
def login():
    if ['username', 'password'] not in request.json.keys():
        return {"type": "error", "message": "Username or password fields not filled"}, 400
    if 'token' in request.json.keys():
        if decode_auth_token('token')[0]:
            return {"type": "message", "message": "Already logged in"}

    if user := User.query.filter_by(username=request.json['username']):
        if bcrypt.check_password_hash(user.password, request.json['password']):
            return {"type": "success", "message": "User authenticated", "token": encode_auth_token(user.username)}
        else:
            return {"type": "error", "message": "Incorrect password"}
    else:
        return {"type": "error", "message": "Incorrect "}


