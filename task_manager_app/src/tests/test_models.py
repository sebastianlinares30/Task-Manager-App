"""
Unit tests for the Task and User model classes.
"""

from models.task import Task
from models.user import User


def test_task_stores_basic_information():
    """Verify that a Task object stores the provided task information."""
    task = Task(
        task_id=1,
        user_id=2,
        task_name="Study",
        due_date="2026/07/30",
        task_description="Study chapter 8"
    )

    assert task.task_id == 1
    assert task.user_id == 2
    assert task.task_name == "Study"
    assert task.due_date == "2026/07/30"
    assert task.task_description == "Study chapter 8"


def test_task_uses_default_values():
    """Verify that a Task object uses the expected default values."""
    task = Task()

    assert task.task_id is None
    assert task.user_id is None
    assert task.task_name == ""
    assert task.due_date == ""
    assert task.task_description == ""
    assert task.priority is None
    assert task.status is None


def test_user_stores_login_information():
    """Verify that a User object stores login credentials correctly."""
    user = User(
        email="test@test.com",
        password="test123"
    )

    assert user.email == "test@test.com"
    assert user.password == "test123"


def test_user_stores_signup_information():
    """Verify that a User object stores signup information correctly."""
    user = User(
        user_id=1,
        first_name="Dario",
        last_name="Miranda",
        email="test@test.com",
        password="test123"
    )

    assert user.user_id == 1
    assert user.first_name == "Dario"
    assert user.last_name == "Miranda"