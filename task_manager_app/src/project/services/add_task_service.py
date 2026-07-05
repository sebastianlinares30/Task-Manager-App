from models.task import Task
from repositories.task_repository import TaskRepository


class AddTaskService:
    """
    Handles the application logic for adding tasks.
    """

    def __init__(self) -> None:
        self.task_repository = TaskRepository()

    def add_task(self, task: Task) -> dict:
        self.task_repository.add_task(task)

        return {"success": True}