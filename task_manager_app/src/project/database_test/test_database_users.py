"""
test_database_users.py

Displays the users currently registered in the local SQLite database.

This file is used as a manual inspection test. It helps the team verify
that user accounts created through the Sign Up page are being stored
correctly in the users table. Passwords are not displayed for safety.
"""

import sqlite3
from pathlib import Path


# Move from database_test/ back to project/
# so the test can find database/taskapp.db correctly.
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "taskapp.db"


print("=" * 50)
print("        REGISTERED USERS")
print("=" * 50)

print(f"\nDatabase File: {DATABASE_PATH.name}")
print(f"Database Exists: {'Yes' if DATABASE_PATH.exists() else 'No'}")


# Open a connection to the local SQLite database.
conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()


# -----------------------------
# USERS
# -----------------------------

# Retrieve registered users without displaying passwords.
cursor.execute("""
    SELECT id, first_name, last_name, email
    FROM users
    ORDER BY id
""")

users = cursor.fetchall()

if users:

    print(f"\nTotal Registered Users: {len(users)}\n")

    print(
        f"{'ID':<5}"
        f"{'First Name':<15}"
        f"{'Last Name':<15}"
        f"{'Email'}"
    )
    print("-" * 60)

    for user in users:
        print(
            f"{user[0]:<5}"
            f"{user[1]:<15}"
            f"{user[2]:<15}"
            f"{user[3]}"
        )

else:
    print("\nNo registered users found.")


# Always close the database connection after the test finishes.
conn.close()

print("\nUser inspection completed successfully.")
