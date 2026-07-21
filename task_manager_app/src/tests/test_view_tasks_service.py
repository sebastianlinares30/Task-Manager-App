"""
Unit tests for the ViewTasksService class.
"""

from unittest.mock import Mock

from services.view_tasks_service import ViewTasksService


def test_get_tasks_returns_task_list():
    """Verify that the service returns the task list from the repository."""
    service = ViewTasksService()
    service.task_repository = Mock()

    expected = ["Task 1", "Task 2"]

    service.task_repository.get_tasks_by_user.return_value = expected

    result = service.get_tasks(5)

    assert result == expected


def test_get_tasks_calls_repository():
    """Verify that the service passes the user ID to the repository."""
    service = ViewTasksService()
    service.task_repository = Mock()

    service.task_repository.get_tasks_by_user.return_value = []

    service.get_tasks(3)

    service.task_repository.get_tasks_by_user.assert_called_once_with(3)


def test_get_tasks_returns_empty_list():
    """Verify that the service returns an empty list when no tasks are found."""
    service = ViewTasksService()
    service.task_repository = Mock()

    service.task_repository.get_tasks_by_user.return_value = []

    result = service.get_tasks(10)

    assert result == []