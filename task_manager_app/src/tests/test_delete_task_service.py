"""
Unit tests for the DeleteTaskService class.
"""

from unittest.mock import Mock

from services.delete_task_service import DeleteTaskService


def test_delete_task_returns_success():
    """Verify that deleting a task returns a successful response."""
    service = DeleteTaskService()
    service.task_repository = Mock()

    service.task_repository.delete_task.return_value = True

    result = service.delete_task(5, 2)

    assert result == {"success": True}


def test_delete_task_calls_repository():
    """Verify that the service passes the task ID and user ID to the repository."""
    service = DeleteTaskService()
    service.task_repository = Mock()

    service.task_repository.delete_task.return_value = True

    service.delete_task(10, 2)

    service.task_repository.delete_task.assert_called_once_with(10, 2)


def test_delete_task_returns_dictionary():
    """Verify that the service returns a dictionary response."""
    service = DeleteTaskService()
    service.task_repository = Mock()

    service.task_repository.delete_task.return_value = True

    result = service.delete_task(1, 2)

    assert isinstance(result, dict)

def test_delete_task_returns_failure_for_wrong_user():
    """Verify that deleting a task owned by another user returns failure."""
    service = DeleteTaskService()
    service.task_repository = Mock()

    service.task_repository.delete_task.return_value = False

    result = service.delete_task(5, 2)

    assert result == {
        "success": False,
        "message": "Task not found or does not belong to this user."
    }