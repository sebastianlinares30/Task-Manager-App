# Testing Summary

To complete the current milestone, the team used **pytest** and **coverage.py** to test the main features of the Task Manager application. In the project, there are currently **33 automated tests**, which include **31 unit tests** and **2 integration tests**.

The unit tests check the `Task` and `User` models in terms of their attributes and default values. In addition, these tests check such services as **login**, **sign-up**, **add-task**, **view-tasks**, and **delete-task** with the help of mocked repositories and ensure that each service calls the respective repository method with the expected data.

Repository tests ensure the right performance of database operations executed by the `UserRepository` and `TaskRepository`. These tests ensure that the respective repositories run SQL queries with the required parameters to create users, find users by email, add tasks, find tasks for the user, and delete tasks using both the task ID and user ID. Besides, the tests ensure that all database changes are committed and that the connections are properly closed.

The integration tests are used to ensure the proper interaction of the **service layer**, **repository layer**, and a temporary **SQLite** database in the course of task management processes. One integration test checks whether the task created in the service layer can be found in the database. Another one checks the entire workflow of adding, finding, deleting, and confirming that the task was deleted.

As a result, the automated tests check **user authentication**, **user registration**, **task creation**, **task finding**, **task deletion**, **model behavior**, **operations with the database**, and **interaction between the layers** of the application that was tested. The authentication tests were also updated after implementing password hashing, and the task deletion tests now verify the user ID together with the task ID to support task ownership.

All **33 tests** have passed successfully, and the generated coverage report shows approximately **99% code coverage of the model, service, and repository files included in the report**.

## Issues Found During Testing

During manual testing, an issue was discovered when attempting to access the application through:

```text
http://127.0.0.1:5000
```

The application returned a **404 Not Found** error because the root route (`/`) had not been configured in Flask. Although the frontend pages already existed, there was no route serving the initial page.

To resolve the issue, a `PageController` was created to manage the application's page routes, including the root URL (`/`). After adding the missing route, Flask served the application's initial page correctly, and the application loaded successfully from the default Flask address.

## Coverage Reports

The generated reports are available in:

- `docs/tests/coverage_report.txt`
- `docs/tests/htmlcov/`
