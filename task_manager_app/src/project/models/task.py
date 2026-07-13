#task

class Task:
    """
    Represents a task object used across the application.
    """

    def __init__(
        self,
        task_id: int = None,
        user_id: int = None,
        task_name: str = "",
        due_date: str = "",
        task_description: str = "",
        priority: str = None,
        status: str = None
    ) -> None:
        self.task_id = task_id
        self.user_id = user_id
        self.task_name = task_name
        self.due_date = due_date
        self.task_description = task_description
        self.priority = priority
        self.status = status