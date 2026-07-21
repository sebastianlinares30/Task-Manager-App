"""
Unit tests for the AddTaskService class.
"""

from unittest.mock import Mock

from models.task import Task
from services.add_task_service import AddTaskService


def test_add_task_returns_success():
    """Verify that adding a task returns a successful response."""
    service = AddTaskService()
    service.task_repository = Mock()

    task = Task(
        user_id=1,
        task_name="Study",
        due_date="2026/07/20",
        task_description="Chapter 8"
    )

    result = service.add_task(task)

    assert result == {"success": True}


def test_add_task_calls_repository():
    """Verify that the service sends the Task object to the repository."""
    service = AddTaskService()
    service.task_repository = Mock()

    task = Task(
        user_id=1,
        task_name="Study",
        due_date="2026/07/20",
        task_description="Chapter 8"
    )

    service.add_task(task)

    service.task_repository.add_task.assert_called_once_with(task)


def test_add_task_returns_dictionary():
    """Verify that the service returns a dictionary response."""
    service = AddTaskService()
    service.task_repository = Mock()

    task = Task()

    result = service.add_task(task)

    assert isinstance(result, dict)