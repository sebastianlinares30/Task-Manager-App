from flask import Blueprint, request, jsonify

from models.user import User
from services.sign_up_service import SignUpService


sign_up_bp = Blueprint("sign_up", __name__)


@sign_up_bp.route("/sign-up", methods=["POST"])
def sign_up():
    data = request.get_json()

    user = User(
        first_name=data["first_name"],
        last_name=data["last_name"],
        email=data["email"],
        password=data["password"]
    )

    service = SignUpService()
    result = service.create_user(user)

    return jsonify(result)