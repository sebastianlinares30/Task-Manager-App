from flask import Blueprint, request, jsonify, session

from models.task import Task
from services.add_task_service import AddTaskService


add_task_bp = Blueprint("add_task", __name__)


@add_task_bp.route("/add-task", methods=["POST"])
def add_task():
    data = request.get_json()

    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    task = Task(
        user_id=user_id,
        task_name=data["task_name"],
        due_date=data["due_date"],
        task_description=data["task_description"]
    )

    service = AddTaskService()
    result = service.add_task(task)

    return jsonify(result)