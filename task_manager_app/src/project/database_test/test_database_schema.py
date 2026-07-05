import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "taskapp.db"

print("=" * 45)
print("        USERS TABLE SCHEMA")
print("=" * 45)

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(users)")
columns = cursor.fetchall()

print(f"\n{'Column Name':<18}{'Type':<12}{'Required':<12}{'Primary Key'}")
print("-" * 55)

for column in columns:
    name = column[1]
    data_type = column[2]
    required = "Yes" if column[3] else "No"
    primary_key = "Yes" if column[5] else "No"

    print(f"{name:<18}{data_type:<12}{required:<12}{primary_key}")

conn.close()

print("\nSchema inspection completed successfully.")