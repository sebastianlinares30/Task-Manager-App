# Task Manager App

This project is a web-based Task Manager application built with Flask following the MVC architecture. The application uses SQLite for data storage and includes automated unit and integration tests to validate the core functionality.

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

## Tools Used

- Flask
- SQLite
- pytest
- coverage.py

## Coverage

The project currently contains **32 automated tests**, including **30 unit tests** and **2 integration tests**, with approximately **99% code coverage**.
