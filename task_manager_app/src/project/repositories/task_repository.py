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
            INSERT INTO tasks (user_id, task_name, due_date, description)
            VALUES (?, ?, ?, ?)
            """,
            (task.user_id, task.task_name, task.due_date, task.task_description)
        )

        conn.commit()
        # will remove the close connection beucase other need to use the same instance so we dont want one person to close it
        conn.close()

    def get_tasks_by_user(self, user_id: int) -> list[Task]:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id, user_id, task_name, due_date, description
            FROM tasks
            WHERE user_id = ?
            """,
            (user_id,)
        )

        rows = cursor.fetchall()
        # will remove the close connection beucase other need to use the same instance so we dont want one person to close it
        conn.close()

        tasks = []

        for row in rows:
            task = Task(
                task_id=row[0],
                user_id=row[1],
                task_name=row[2],
                due_date=row[3],
                task_description=row[4]
            )

            tasks.append(task)

        return tasks

    """
    Deletes a task from the database using its unique identifier.
    """
    def delete_task(self, task_id: int, user_id: int) -> bool:

        # Open a connection to the SQLite database.
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM tasks
            WHERE id = ? AND user_id = ?
            """,
            (task_id, user_id)
        )

        deleted = cursor.rowcount > 0

        # Save the changes and release the database connection.
        conn.commit()
        # will remove the close connection beucase other need to use the same instance so we dont want one person to close it
        conn.close()

        return deleted
