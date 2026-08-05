from werkzeug.security import check_password_hash

from repositories.user_repository import UserRepository


class LoginService:
    """
    Handles the application logic for user login.
    """

    def __init__(self) -> None:
        self.user_repository = UserRepository()

    def login(self, user) -> dict:
        result = self.user_repository.find_user_by_email(user.email)

        if result:
            user_id = result[0]
            stored_password = result[1]

            if check_password_hash(stored_password, user.password):
                return {
                    "success": True,
                    "user_id": result[0]
                }

        return {
            "success": False
        }