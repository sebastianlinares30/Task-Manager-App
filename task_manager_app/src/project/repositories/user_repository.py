from core.database import get_connection
from models.user import User


class UserRepository:
    """
    Handles database operations related to users.
    """

    def find_user_by_email_and_password(self, user: User):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id
            FROM users
            WHERE email = ? AND password = ?
            """,
            (user.email, user.password)
        )

        result = cursor.fetchone()
        # will remove the close connection beucase other need to use the same instance so we dont want one person to close it
        conn.close()

        return result
    
    def create_user(self, user: User) -> None:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users (first_name, last_name, email, password)
            VALUES (?, ?, ?, ?)
            """,
        (user.first_name, user.last_name, user.email, user.password)
    )

        conn.commit()
        # will remove the close connection beucase other need to use the same instance so we dont want one person to close it
        conn.close()
