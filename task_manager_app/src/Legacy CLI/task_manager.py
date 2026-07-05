#TaskManager

from datetime import datetime

from task import Task
from menu import Menu


class TaskManager:
    """
    Manages tasks and handles user interaction for the Task Manager application.
    """

    def __init__(self) -> None:
        """
        Initializes the Task Manager.

        Creates an empty task list and initializes the menu.

        Returns:
            None
        """
        self.tasks = []
        self.menu = Menu()

    def get_due_date(self) -> datetime:
        """
        Prompts the user to enter a valid due date.

        The user must enter the date in MM/DD/YYYY format.

        Returns:
            datetime: The validated due date.

        Handles:
            ValueError: Raised internally when the input cannot be
            parsed as a valid date. The exception is caught and the
            user is prompted to enter the date again.
        """
        while True:
            date_str = input("Due Date (MM/DD/YYYY): ")

            try:
                return datetime.strptime(date_str, "%m/%d/%Y")

            except ValueError:
                print("Invalid date. Please use MM/DD/YYYY.")

    def add_task(self) -> None:
        """
        Creates a new task and adds it to the task list.

        Returns:
            None

        Handles:
            ValueError: Raised internally when the user enters a
            non-numeric value. The exception is caught and an error
            message is displayed.
        """
        name = input("Task name: ")
        due_date = self.get_due_date()

        task = Task(name, due_date)
        self.tasks.append(task)

    def view_tasks(self) -> None:
        """
        Displays all tasks and their due dates.

        Returns:
            None
        """
        for task in self.tasks:
            print(task.name, task.due_date.strftime("%m/%d/%Y"))

    def delete_task(self) -> None:
        """
        Removes a task selected by the user.

        Displays all available tasks and prompts the user
        to select one for deletion.

        Returns:
            None
        """
        if not self.tasks:
            print("No tasks available.")
            return

        print("\nTasks:")

        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task.name}")

        try:
            choice = int(input("\nSelect task to delete: "))

            if 1 <= choice <= len(self.tasks):
                removed_task = self.tasks.pop(choice - 1)
                print(f"{removed_task.name} deleted.")
            else:
                print("Invalid selection.")

        except ValueError:
            print("Please enter a number.")

    def run(self) -> None:
        """
        Runs the main application loop.

        Continuously displays the menu and processes
        the user's selection until the user exits.

        Returns:
            None
        """
        while True:
            self.menu.display()

            choice = input("Choice: ")

            if choice == "1":
                self.add_task()

            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                self.delete_task()

            elif choice == "4":
                break