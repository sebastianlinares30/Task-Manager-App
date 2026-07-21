"""
Unit tests for the TaskRepository class.
"""

from unittest.mock import Mock, patch

from models.task import Task
from repositories.task_repository import TaskRepository


@patch("repositories.task_repository.get_connection")
def test_add_task_inserts_task_information(mock_get_connection):
    """Verify that add_task executes an INSERT query with the correct task data."""
    mock_connection = Mock()
    mock_cursor = Mock()

    mock_get_connection.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor

    repository = TaskRepository()

    task = Task(
        user_id=2,
        task_name="Study",
        due_date="2026/07/30",
        task_description="Study chapter 8"
    )

    repository.add_task(task)

    query, parameters = mock_cursor.execute.call_args.args

    assert "INSERT INTO tasks" in query
    assert parameters == (
        2,
        "Study",
        "2026/07/30",
        "Study chapter 8"
    )


@patch("repositories.task_repository.get_connection")
def test_add_task_commits_and_closes_connection(mock_get_connection):
    """Verify that add_task commits the transaction and closes the connection."""
    mock_connection = Mock()
    mock_cursor = Mock()

    mock_get_connection.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor

    repository = TaskRepository()
    task = Task(task_name="Test task")

    repository.add_task(task)

    mock_connection.commit.assert_called_once()
    mock_connection.close.assert_called_once()


@patch("repositories.task_repository.get_connection")
def test_get_tasks_returns_task_objects(mock_get_connection):
    """Verify that database rows are converted into Task objects."""
    mock_connection = Mock()
    mock_cursor = Mock()

    mock_get_connection.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor

    mock_cursor.fetchall.return_value = [
        (1, 5, "Study", "2026/07/30", "Chapter 8"),
        (2, 5, "Homework", "2026/08/01", "Complete assignment")
    ]

    repository = TaskRepository()

    result = repository.get_tasks_by_user(5)

    assert len(result) == 2
    assert isinstance(result[0], Task)
    assert result[0].task_id == 1
    assert result[0].task_name == "Study"
    assert result[0].task_description == "Chapter 8"
    assert result[1].task_id == 2
    assert result[1].task_name == "Homework"


@patch("repositories.task_repository.get_connection")
def test_get_tasks_executes_query_with_user_id(mock_get_connection):
    """Verify that get_tasks_by_user uses the correct user ID in the query."""
    mock_connection = Mock()
    mock_cursor = Mock()

    mock_get_connection.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = []

    repository = TaskRepository()

    repository.get_tasks_by_user(7)

    query, parameters = mock_cursor.execute.call_args.args

    assert "SELECT id, user_id, task_name, due_date, description" in query
    assert "WHERE user_id = ?" in query
    assert parameters == (7,)


@patch("repositories.task_repository.get_connection")
def test_get_tasks_returns_empty_list(mock_get_connection):
    """Verify that no database rows result in an empty task list."""
    mock_connection = Mock()
    mock_cursor = Mock()

    mock_get_connection.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = []

    repository = TaskRepository()

    result = repository.get_tasks_by_user(10)

    assert result == []
    mock_connection.close.assert_called_once()


@patch("repositories.task_repository.get_connection")
def test_delete_task_executes_query_with_task_id(mock_get_connection):
    """Verify that delete_task executes a DELETE query with the correct task ID."""
    mock_connection = Mock()
    mock_cursor = Mock()

    mock_get_connection.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor

    repository = TaskRepository()

    repository.delete_task(12)

    query, parameters = mock_cursor.execute.call_args.args

    assert "DELETE FROM tasks" in query
    assert "WHERE id = ?" in query
    assert parameters == (12,)


@patch("repositories.task_repository.get_connection")
def test_delete_task_commits_and_closes_connection(mock_get_connection):
    """Verify that delete_task commits the transaction and closes the connection."""
    mock_connection = Mock()
    mock_cursor = Mock()

    mock_get_connection.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor

    repository = TaskRepository()

    repository.delete_task(3)

    mock_connection.commit.assert_called_once()
    mock_connection.close.assert_called_once()