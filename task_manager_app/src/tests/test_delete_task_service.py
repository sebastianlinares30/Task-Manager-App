"""
Unit tests for the DeleteTaskService class.
"""

from unittest.mock import Mock

from services.delete_task_service import DeleteTaskService


def test_delete_task_returns_success():
    """Verify that deleting a task returns a successful response."""
    service = DeleteTaskService()
    service.task_repository = Mock()

    result = service.delete_task(5)

    assert result == {"success": True}


def test_delete_task_calls_repository():
    """Verify that the service passes the task ID to the repository."""
    service = DeleteTaskService()
    service.task_repository = Mock()

    service.delete_task(10)

    service.task_repository.delete_task.assert_called_once_with(10)


def test_delete_task_returns_dictionary():
    """Verify that the service returns a dictionary response."""
    service = DeleteTaskService()
    service.task_repository = Mock()

    result = service.delete_task(1)

    assert isinstance(result, dict)