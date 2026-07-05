from models.task import Task
from repositories.task_repository import TaskRepository


class ViewTasksService:
    """
    Handles the application logic for retrieving tasks.
    """

    def __init__(self) -> None:
        self.task_repository = TaskRepository()

    def get_tasks(self, user_id: int) -> list[Task]:
        return self.task_repository.get_tasks_by_user(user_id)