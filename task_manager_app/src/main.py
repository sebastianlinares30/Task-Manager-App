#main

from task_manager import TaskManager


def main() -> None:
    """
    Starts the Task Manager application.

    This function creates an instance of TaskManager
    and runs the main application loop.

    Returns:
        None
    """
    app = TaskManager()
    app.run()


if __name__ == "__main__":
    main()