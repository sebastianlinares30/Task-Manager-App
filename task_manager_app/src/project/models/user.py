class User:
    """
    Represents a user object used across the web application.
    """

    def __init__(
        self,
        email: str,
        password: str,
        user_id: int = None,
        first_name: str = None,
        last_name: str = None
    ) -> None:
        
        
        self.user_id = user_id
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name