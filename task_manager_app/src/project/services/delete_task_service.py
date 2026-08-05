"""
delete_task_service.py

Contains the application logic for deleting tasks.

Responsibilities:
- Validate the delete request.
- Communicate with the TaskRepository.
- Return the operation result to the controller.
"""

from repositories.task_repository import TaskRepository

class DeleteTaskService:
    """
    Handles the application logic for deleting tasks.
    """

    def __init__(self) -> None:
        # Repository used to access task data.
        self.task_repository = TaskRepository()

    def delete_task(self, task_id: int, user_id: int) -> dict:

        deleted = self.task_repository.delete_task(task_id, user_id)

        if not deleted:
            return {
                "success": False,
             "message": "Task not found or does not belong to this user."
            }

        # Inform the controller that the operation completed successfully.
        return {"success": True}