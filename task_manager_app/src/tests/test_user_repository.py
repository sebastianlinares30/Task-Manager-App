"""
Unit tests for the UserRepository class.
"""

from unittest.mock import Mock, patch

from models.user import User
from repositories.user_repository import UserRepository


@patch("repositories.user_repository.get_connection")
def test_find_user_returns_matching_user(mock_get_connection):
    """Verify that the repository returns the matching user data."""
    mock_connection = Mock()
    mock_cursor = Mock()

    mock_get_connection.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = (4, "hashed_password")

    repository = UserRepository()

    result = repository.find_user_by_email("test@test.com")

    assert result == (4, "hashed_password")


@patch("repositories.user_repository.get_connection")
def test_find_user_executes_query_with_email(mock_get_connection):
    """Verify that the repository executes the query with the provided email."""
    mock_connection = Mock()
    mock_cursor = Mock()

    mock_get_connection.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = None

    repository = UserRepository()

    repository.find_user_by_email("user@test.com")

    mock_cursor.execute.assert_called_once_with(
        """
            SELECT id, password
            FROM users
            WHERE email = ?
            """,
        ("user@test.com",)
    )


@patch("repositories.user_repository.get_connection")
def test_find_user_closes_connection(mock_get_connection):
    """Verify that the database connection is closed after searching for a user."""
    mock_connection = Mock()
    mock_cursor = Mock()

    mock_get_connection.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = None

    repository = UserRepository()

    repository.find_user_by_email("test@test.com")

    mock_connection.close.assert_called_once()


@patch("repositories.user_repository.get_connection")
def test_create_user_inserts_user_information(mock_get_connection):
    """Verify that create_user executes an INSERT query with the correct user data."""
    mock_connection = Mock()
    mock_cursor = Mock()

    mock_get_connection.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor

    repository = UserRepository()

    user = User(
        first_name="Dario",
        last_name="Miranda",
        email="dario@test.com",
        password="test123"
    )

    repository.create_user(user)

    query, parameters = mock_cursor.execute.call_args.args

    assert "INSERT INTO users" in query
    assert parameters == (
        "Dario",
        "Miranda",
        "dario@test.com",
        "test123"
    )


@patch("repositories.user_repository.get_connection")
def test_create_user_commits_and_closes_connection(mock_get_connection):
    """Verify that create_user commits the transaction and closes the connection."""
    mock_connection = Mock()
    mock_cursor = Mock()

    mock_get_connection.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor

    repository = UserRepository()

    user = User(
        first_name="Test",
        last_name="User",
        email="new@test.com",
        password="password"
    )

    repository.create_user(user)

    mock_connection.commit.assert_called_once()
    mock_connection.close.assert_called_once()