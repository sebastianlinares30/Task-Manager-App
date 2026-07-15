"""
test_database_schema.py

Displays the schema of the users and tasks tables in the local SQLite
database.

This file is used as a manual inspection test. It helps the team verify
that both tables contain the expected columns, data types, required
(NOT NULL) fields, and primary key configuration.
"""

import sqlite3
from pathlib import Path


# Move from database_test/ back to project/
# so the test can find database/taskapp.db correctly.
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "taskapp.db"


print("=" * 55)
print("        TASK MANAGER DATABASE SCHEMA")
print("=" * 55)

# Open a connection to the local SQLite database.
conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()


def display_table_schema(table_name):
    """
    Displays the schema information for a database table.

    Args:
        table_name (str): Name of the table being inspected.
    """

    print(f"\n{table_name.upper()} TABLE")
    print("-" * 55)

    # Retrieve the schema information for the selected table.
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()

    if columns:
        print(
            f"{'Column Name':<18}"
            f"{'Type':<12}"
            f"{'Required':<12}"
            f"{'Primary Key'}"
        )
        print("-" * 55)

        for column in columns:
            name = column[1]
            data_type = column[2]

            # PRAGMA returns 1 when the column has a NOT NULL constraint.
            required = "Yes" if column[3] else "No"

            # PRAGMA returns 1 when the column is the table's primary key.
            primary_key = "Yes" if column[5] else "No"

            print(
                f"{name:<18}"
                f"{data_type:<12}"
                f"{required:<12}"
                f"{primary_key}"
            )
    else:
        print(f"The {table_name} table was not found.")


# -----------------------------
# USERS TABLE
# -----------------------------

display_table_schema("users")


# -----------------------------
# TASKS TABLE
# -----------------------------

display_table_schema("tasks")


# Always close the database connection after the test finishes.
conn.close()

print("\nDatabase schema inspection completed successfully.")