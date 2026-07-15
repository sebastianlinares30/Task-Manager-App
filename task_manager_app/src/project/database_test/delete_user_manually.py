"""
delete_user_manually.py

Deletes a selected user and all tasks associated with that user from
the local SQLite database.

This file is intended for manual database maintenance during development.
It verifies the user, requests confirmation, and deletes the user's tasks
before deleting the user account.
"""

import sqlite3
from pathlib import Path


# Move from database_test/ back to project/
# so the script can find database/taskapp.db correctly.
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "taskapp.db"


print("=" * 50)
print("        DELETE USER MANUALLY")
print("=" * 50)

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

try:
    user_id = int(input("\nEnter the user ID to delete: "))

    # Retrieve the selected user.
    cursor.execute("""
        SELECT id, first_name, last_name, email
        FROM users
        WHERE id = ?
    """, (user_id,))

    user = cursor.fetchone()

    if user is None:
        print(f"\nNo user was found with ID {user_id}.")

    else:
        # Count the tasks associated with the selected user.
        cursor.execute("""
            SELECT COUNT(*)
            FROM tasks
            WHERE user_id = ?
        """, (user_id,))

        task_count = cursor.fetchone()[0]

        print("\nUser found:")
        print(f"ID: {user[0]}")
        print(f"Name: {user[1]} {user[2]}")
        print(f"Email: {user[3]}")
        print(f"Associated tasks: {task_count}")

        confirmation = input(
            "\nDelete this user and all associated tasks? (yes/no): "
        ).strip().lower()

        if confirmation == "yes":
            # Delete the user's tasks first to prevent orphan records.
            cursor.execute("""
                DELETE FROM tasks
                WHERE user_id = ?
            """, (user_id,))

            deleted_tasks = cursor.rowcount

            # Delete the user account.
            cursor.execute("""
                DELETE FROM users
                WHERE id = ?
            """, (user_id,))

            deleted_users = cursor.rowcount

            # Save both deletions as one transaction.
            conn.commit()

            print("\nDeletion completed successfully.")
            print(f"Users deleted: {deleted_users}")
            print(f"Tasks deleted: {deleted_tasks}")

        else:
            print("\nDeletion canceled. No records were changed.")

except ValueError:
    print("\nInvalid user ID. Please enter a whole number.")

except sqlite3.Error as error:
    # Undo any incomplete changes if a database error occurs.
    conn.rollback()
    print(f"\nDatabase error: {error}")

finally:
    conn.close()
    print("\nDatabase connection closed.")