"""
test_database_data.py

Displays the current data stored in the local SQLite database.

This file is used as a manual inspection test. It helps the team verify
that users and tasks, including task descriptions, are being saved
correctly in taskapp.db.
"""

import sqlite3
from pathlib import Path


# Move from database_test/ back to project/
# so the test can find database/taskapp.db correctly.
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "taskapp.db"


print("=" * 50)
print("        TASK MANAGER DATABASE")
print("=" * 50)

# Open a connection to the local SQLite database.
conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()


# -----------------------------
# USERS
# -----------------------------

print("\nUSERS")
print("-" * 50)

# Retrieve users without printing passwords for safety.
cursor.execute("""
    SELECT id, first_name, last_name, email
    FROM users
""")

users = cursor.fetchall()

if users:
    print(f"{'ID':<5}{'First Name':<15}{'Last Name':<15}{'Email'}")
    print("-" * 50)

    for user in users:
        print(f"{user[0]:<5}{user[1]:<15}{user[2]:<15}{user[3]}")
else:
    print("No users found.")


# -----------------------------
# TASKS
# -----------------------------

print("\nTASKS")
print("-" * 100)

# Retrieve tasks and show which user each task belongs to.
cursor.execute("""
    SELECT id, user_id, task_name, description, due_date
    FROM tasks
""")

tasks = cursor.fetchall()

if tasks:
    print(
        f"{'ID':<5}"
        f"{'User':<8}"
        f"{'Task':<30}"
        f"{'Description':<35}"
        f"{'Due Date'}"
    )
    print("-" * 100)

    for task in tasks:
        description = (
            task[3]
            if task[3] is not None and task[3] != ""
            else "No description"
        )

        due_date = (
            task[4]
            if task[4] is not None and task[4] != ""
            else "No due date"
        )

        print(
            f"{task[0]:<5}"
            f"{task[1]:<8}"
            f"{task[2]:<30}"
            f"{description:<35}"
            f"{due_date}"
        )
else:
    print("No tasks found.")


# Always close the database connection after the test finishes.
conn.close()

print("\nDatabase inspection completed successfully.")