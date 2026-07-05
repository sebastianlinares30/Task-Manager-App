"""
Registers all application routes (controllers).

Every new feature should be registered here so the
application knows which endpoints are available.
"""


from controllers.login_controller import login_bp
from controllers.add_task_controller import add_task_bp
from controllers.view_tasks_controller import view_tasks_bp
from controllers.sign_up_controller import sign_up_bp
from controllers.delete_task_controller import delete_task_bp


def register_routes(app):
    """
    Registers all controllers with the Flask application.
    """

    app.register_blueprint(login_bp)
    app.register_blueprint(add_task_bp)
    app.register_blueprint(view_tasks_bp)
    app.register_blueprint(sign_up_bp)
    app.register_blueprint(delete_task_bp)