from models.task import Task
from repositories.task_repository import TaskRepository


class AddTaskService:
    """
    Handles the application logic for adding tasks.
    """

    def __init__(self) -> None:
        # we will pass the singleton instance or reference it here.
        # self.task_repository = task_repository_instance
        self.task_repository = TaskRepository()

    def add_task(self, task: Task) -> dict:
        self.task_repository.add_task(task)

        return {"success": True}

# 1. Create a single, shared instance of the Repository
# task_repository_instance = TaskRepository()

# 2. Create a single, shared instance of the Service
# add_task_service_instance = AddTaskService()
