"""
Integration tests for task workflows.

These tests verify that the service and repository layers work together
using a temporary SQLite database.
"""

import sqlite3

from models.task import Task
from services.add_task_service import AddTaskService
from services.view_tasks_service import ViewTasksService
from services.delete_task_service import DeleteTaskService


def test_add_and_view_task_integration(tmp_path, monkeypatch):
    """
    Verify that a task added through the service can be retrieved
    from a temporary SQLite database.
    """

    database_path = tmp_path / "test_taskapp.db"

    connection = sqlite3.connect(database_path)

    connection.execute(
        """
        CREATE TABLE tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            task_name TEXT NOT NULL,
            due_date TEXT,
            description TEXT
        )
        """
    )

    connection.commit()
    connection.close()

    def get_test_connection():
        return sqlite3.connect(database_path)

    monkeypatch.setattr(
        "repositories.task_repository.get_connection",
        get_test_connection
    )

    task = Task(
        user_id=7,
        task_name="Complete Milestone 5",
        due_date="2026/07/25",
        task_description="Finish integration testing"
    )

    add_service = AddTaskService()
    add_result = add_service.add_task(task)

    view_service = ViewTasksService()
    tasks = view_service.get_tasks(7)

    assert add_result == {"success": True}
    assert len(tasks) == 1
    assert tasks[0].user_id == 7
    assert tasks[0].task_name == "Complete Milestone 5"
    assert tasks[0].due_date == "2026/07/25"
    assert tasks[0].task_description == "Finish integration testing"



def test_add_delete_and_view_task_integration(tmp_path, monkeypatch):
    """
    Verify that a task can be added, deleted, and no longer retrieved.
    """

    database_path = tmp_path / "test_taskapp.db"

    connection = sqlite3.connect(database_path)

    connection.execute(
        """
        CREATE TABLE tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            task_name TEXT NOT NULL,
            due_date TEXT,
            description TEXT
        )
        """
    )

    connection.commit()
    connection.close()

    def get_test_connection():
        return sqlite3.connect(database_path)

    monkeypatch.setattr(
        "repositories.task_repository.get_connection",
        get_test_connection
    )

    task = Task(
        user_id=7,
        task_name="Task to delete",
        due_date="2026/07/25",
        task_description="Temporary integration test task"
    )

    AddTaskService().add_task(task)

    tasks_before_delete = ViewTasksService().get_tasks(7)

    assert len(tasks_before_delete) == 1

    task_id = tasks_before_delete[0].task_id

    delete_result = DeleteTaskService().delete_task(task_id, 7)

    tasks_after_delete = ViewTasksService().get_tasks(7)

    assert delete_result == {"success": True}
    assert tasks_after_delete == []