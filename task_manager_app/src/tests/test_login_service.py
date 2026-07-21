"""
Unit tests for the LoginService class.
"""

from unittest.mock import Mock

from models.user import User
from services.login_service import LoginService


def test_login_returns_success_for_valid_credentials():
    """Verify that valid credentials return a successful login response."""
    service = LoginService()
    service.user_repository = Mock()
    service.user_repository.find_user_by_email_and_password.return_value = (5,)

    user = User(
        email="test@test.com",
        password="test123"
    )

    result = service.login(user)

    assert result == {
        "success": True,
        "user_id": 5
    }


def test_login_returns_failure_for_invalid_credentials():
    """Verify that invalid credentials return an unsuccessful response."""
    service = LoginService()
    service.user_repository = Mock()
    service.user_repository.find_user_by_email_and_password.return_value = None

    user = User(
        email="test@test.com",
        password="wrong"
    )

    result = service.login(user)

    assert result == {"success": False}


def test_login_passes_user_to_repository():
    """Verify that LoginService sends the User object to the repository."""
    service = LoginService()
    service.user_repository = Mock()
    service.user_repository.find_user_by_email_and_password.return_value = (1,)

    user = User(
        email="user@test.com",
        password="password"
    )

    service.login(user)

    service.user_repository.find_user_by_email_and_password.assert_called_once_with(
        user
    )