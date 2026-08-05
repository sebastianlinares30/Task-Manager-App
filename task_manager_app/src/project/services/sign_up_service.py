from werkzeug.security import generate_password_hash
from models.user import User
from repositories.user_repository import UserRepository

class SignUpService:
    """
    Handles the application logic for creating a new user.
    """

    def __init__(self) -> None:
        self.user_repository = UserRepository()

    def create_user(self, user: User) -> dict:
        user.password = generate_password_hash(user.password)

        self.user_repository.create_user(user)

        return {"success": True}