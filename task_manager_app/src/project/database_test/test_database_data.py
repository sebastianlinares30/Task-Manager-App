"""
test_database_data.py

Displays the current data stored in the local SQLite database.

This file is used as a manual inspection test. It helps the team verify
that users and tasks are being saved correctly in taskapp.db.
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
    print("-" * 60)

    for user in users:
        print(f"{user[0]:<5}{user[1]:<15}{user[2]:<15}{user[3]}")
else:
    print("No users found.")


# -----------------------------
# TASKS
# -----------------------------

print("\nTASKS")
print("-" * 50)

# Retrieve task records and show which user each task belongs to.
cursor.execute("""
    SELECT id, user_id, task_name, due_date
    FROM tasks
""")

tasks = cursor.fetchall()

if tasks:
    print(f"{'ID':<5}{'User':<8}{'Task':<30}{'Due Date'}")
    print("-" * 70)

    for task in tasks:
        print(f"{task[0]:<5}{task[1]:<8}{task[2]:<30}{task[3]}")
else:
    print("No tasks found.")


# Always close the database connection after the test finishes.
conn.close()

print("\nDatabase inspection completed successfully.")