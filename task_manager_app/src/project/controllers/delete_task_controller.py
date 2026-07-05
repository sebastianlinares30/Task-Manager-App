"""
delete_task_controller.py

Receives delete requests from the front-end.

Responsibilities:
- Receive the task selected by the user.
- Pass the request to the service layer.
- Return the operation result as a JSON response.
"""

from flask import Blueprint, request, jsonify

from services.delete_task_service import DeleteTaskService


# Blueprint that exposes the endpoint responsible for deleting tasks.
delete_task_bp = Blueprint("delete_task", __name__)


@delete_task_bp.route("/delete-task", methods=["DELETE"])
def delete_task():
    # Read the JSON data sent by the front-end.
    data = request.get_json()

    # Get the identifier of the task that should be removed.
    task_id = data["task_id"]

    # Delegate the deletion process to the service layer.
    service = DeleteTaskService()
    result = service.delete_task(task_id)

    # Return the result as a JSON response.
    return jsonify(result)