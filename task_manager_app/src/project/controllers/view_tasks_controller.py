from flask import Blueprint, request, jsonify

from services.view_tasks_service import ViewTasksService


view_tasks_bp = Blueprint("view_tasks", __name__)


@view_tasks_bp.route("/get-tasks", methods=["GET"])
def get_tasks():
    """
    Retrieves all tasks associated with a user.
    """

    user_id = request.args.get("user_id")

    service = ViewTasksService()

    tasks = service.get_tasks(user_id)

    response = []

    for task in tasks:
        response.append({
            "task_id": task.task_id,
            "task_name": task.task_name,
            "task_description": task.task_description,
            "due_date": task.due_date
        })

    return jsonify(response)

