"""
test_database_summary.py

Displays a summary of the local SQLite database.

This file is used as a manual inspection test. It helps the team verify
that the database exists, the expected application tables are available,
and the number of records currently stored in each table.
"""

import sqlite3
from pathlib import Path


# Move from database_test/ back to project/
# so the test can find database/taskapp.db correctly.
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "taskapp.db"


print("=" * 50)
print("        DATABASE SUMMARY")
print("=" * 50)

# Verify that the database file exists.
print(f"\nDatabase File: {DATABASE_PATH.name}")
print(f"Database Exists: {'Yes' if DATABASE_PATH.exists() else 'No'}")


# Open a connection to the local SQLite database.
conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()


# -----------------------------
# DATABASE TABLES
# -----------------------------

# Retrieve the application tables while excluding SQLite internal tables.
cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    AND name NOT LIKE 'sqlite_%'
    ORDER BY name
""")

tables = cursor.fetchall()

print("\nAPPLICATION TABLES")
print("-" * 50)

# Display the number of records stored in each table.
for table in tables:

    table_name = table[0]

    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    total_records = cursor.fetchone()[0]

    print(f"{table_name:<15} {total_records} record(s)")


# Always close the database connection after the test finishes.
conn.close()

print("\nDatabase summary completed successfully.")