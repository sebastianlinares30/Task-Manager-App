#TaskManager

from datetime import datetime

from task import Task
from menu import Menu


class TaskManager:

    def __init__(self):
        self.tasks = []
        self.menu = Menu()

    def get_due_date(self):

        while True:

            date_str = input("Due Date (MM/DD/YYYY): ")

            try:
                return datetime.strptime(date_str, "%m/%d/%Y")

            except ValueError:
                print("Invalid date. Please use MM/DD/YYYY.")

    def add_task(self):

        name = input("Task name: ")
        due_date = self.get_due_date()

        task = Task(name, due_date)
        self.tasks.append(task)

    def view_tasks(self):

        for task in self.tasks:
            print(task.name, task.due_date.strftime("%m/%d/%Y"))

    def delete_task(self):

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
    
    def run(self):

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