#class menu

class Menu:
    """
    Displays the menu options for the Task Manager application.
    """

    def display(self) -> None:
        """
        Displays the main menu options to the user.

        Returns:
            None
        """
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")