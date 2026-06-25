#task

from datetime import datetime


class Task:
    """
    Represents a task in the Task Manager application.
    """

    def __init__(self, name: str, due_date: datetime) -> None:
        """
        Initializes a new task.

        Args:
            name (str): The name of the task.
            due_date (datetime): The due date assigned to the task.

        Returns:
            None
        """
        self.name = name
        self.due_date = due_date