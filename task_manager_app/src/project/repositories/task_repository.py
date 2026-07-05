"""
task_repository.py

Handles all database operations related to tasks.

Responsibilities:
- Insert new tasks.
- Retrieve tasks by user.
- Delete tasks.
- Manage future task-related database operations.
"""

from core.database import get_connection
from models.task import Task


class TaskRepository:
    """
    Handles database operations related to tasks.
    """

    def add_task(self, task: Task) -> None:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO tasks (user_id, task_name, due_date)
            VALUES (?, ?, ?)
            """,
            (task.user_id, task.task_name, task.due_date)
        )

        conn.commit()
        conn.close()

    def get_tasks_by_user(self, user_id: int) -> list[Task]:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id, user_id, task_name, due_date
            FROM tasks
            WHERE user_id = ?
            """,
            (user_id,)
        )

        rows = cursor.fetchall()
        conn.close()

        tasks = []

        for row in rows:
            task = Task(
                task_id=row[0],
                user_id=row[1],
                task_name=row[2],
                due_date=row[3]
            )

            tasks.append(task)

        return tasks

    """
    Deletes a task from the database using its unique identifier.
    """
    def delete_task(self, task_id: int) -> None:

        # Open a connection to the SQLite database.
        conn = get_connection()
        cursor = conn.cursor()

        # Delete the task that matches the given identifier.
        cursor.execute(
            """
            DELETE FROM tasks
            WHERE id = ?
            """,
            (task_id,)
        )

        # Save the changes and release the database connection.
        conn.commit()
        conn.close()