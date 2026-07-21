"""
Unit tests for the SignUpService class.
"""

from unittest.mock import Mock

from models.user import User
from services.sign_up_service import SignUpService


def test_signup_returns_success():
    """Verify that creating a new user returns a successful response."""
    service = SignUpService()
    service.user_repository = Mock()

    user = User(
        first_name="Test",
        last_name="User",
        email="new@test.com",
        password="test123"
    )

    result = service.create_user(user)

    assert result == {"success": True}


def test_signup_passes_user_to_repository():
    """Verify that the service passes the User object to the repository."""
    service = SignUpService()
    service.user_repository = Mock()

    user = User(
        first_name="Test",
        last_name="User",
        email="new@test.com",
        password="test123"
    )

    service.create_user(user)

    service.user_repository.create_user.assert_called_once_with(user)