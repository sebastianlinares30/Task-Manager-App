from models.user import User
from repositories.user_repository import UserRepository


class LoginService:
    """
    Handles the application logic for user login.
    """

    def __init__(self) -> None:
        self.user_repository = UserRepository()

    def login(self, user: User) -> dict:
        result = self.user_repository.find_user_by_email_and_password(user)

        if result:
            return {
                "success": True,
                "user_id": result[0]
            }

        return {
            "success": False
        }