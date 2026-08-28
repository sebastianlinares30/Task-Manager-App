# Task Manager App

This project is a web-based Task Manager application built with Flask following the MVC architecture. The application allows multiple users to create accounts and manage their own tasks, including task names, descriptions, and due dates. SQLite is used for data storage, and automated unit and integration tests are included to validate the core functionality.

## Features

The Task Manager application currently supports:

- User registration
- User login and logout
- Add tasks
- View tasks
- Delete tasks
- Task descriptions
- Due dates
- Multiple user accounts

## Running the Application

Navigate to the project directory:

```bash
cd task_manager_app/src/project
```

Start the Flask application:

```bash
python app.py
```

Once the server is running, open your browser and go to:

```text
http://127.0.0.1:5000
```

## Security and Robustness Improvements

The application uses Flask sessions to identify authenticated users instead of relying on user IDs provided by the browser. Passwords are stored using password hashing instead of plain text.

Task operations use the authenticated user's ID, and task deletion verifies task ownership to prevent users from deleting tasks that belong to another user.

## Running the Test Suite

Before running the tests, navigate to the `src` directory:

```bash
cd task_manager_app/src
```

Run all tests:

```bash
python -m pytest tests
```

Generate the coverage report:

```bash
python -m coverage erase
python -m coverage run -m pytest tests
python -m coverage report -m
python -m coverage report -m > ..\docs\tests\coverage_report.txt
python -m coverage html -d ..\docs\tests\htmlcov
```

## View the Coverage Report

To open the saved coverage report from the `src` directory, run:

```powershell
start ..\docs\tests\coverage_report.txt
```

## View the HTML Coverage Report

The HTML coverage report is located in the `docs/tests/htmlcov` directory.

To open it from the `src` directory, run:

```powershell
start ..\docs\tests\htmlcov\index.html
```

## Testing and Refactoring Outcomes

The automated tests cover the model, service, and repository layers of the application. The authentication tests were updated after implementing password hashing, and task deletion tests were updated to verify task ownership using both the task ID and user ID.

During the final development stage, authentication and task ownership were improved to make the application more secure and maintainable. Additional refactoring and robustness improvements will be documented in the final project documentation -Alex-, -Sebastian-.

## Tools Used

- Flask
- SQLite
- pytest
- coverage.py

## Coverage

The project currently contains **33 automated tests**, including **31 unit tests** and **2 integration tests**. The generated report shows approximately **99% code coverage for the model, service, and repository files included in the report**.

## Screenshots

Application screenshots are available in:

- `task_manager_app/docs/screenshots/`

## Contributors

- Dario Miranda
- Sebastian
- Alex
