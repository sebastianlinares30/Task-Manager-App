import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "taskapp.db"

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

print("========== DATABASE SUMMARY ==========\n")

# Show tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]

    print(f"Table: {table_name}")

    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    total = cursor.fetchone()[0]

    print(f"Rows: {total}")

    print("-----------------------------")

conn.close()