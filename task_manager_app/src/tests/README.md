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

- pytest
- coverage.py

## Coverage

The project currently contains **32 automated tests**, including **30 unit tests** and **2 integration tests**, with approximately **99% code coverage**.