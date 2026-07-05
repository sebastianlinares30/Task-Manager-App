from flask import Blueprint, request, jsonify

from models.user import User
from services.login_service import LoginService


login_bp = Blueprint("login", __name__)


@login_bp.route("/login", methods=["POST"])
def login():
    """
    Receives the login request from the frontend.
    Creates a User object and delegates the authentication
    process to the LoginService.
    """

    data = request.get_json()

    user = User(
        email=data["username"],
        password=data["password"]
    )

    service = LoginService()

    result = service.login(user)

    return jsonify(result)