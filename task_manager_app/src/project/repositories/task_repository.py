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
            SELECT task_name, due_date
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
                user_id=user_id,
                task_name=row[0],
                due_date=row[1]
            )

            tasks.append(task)

        return tasks