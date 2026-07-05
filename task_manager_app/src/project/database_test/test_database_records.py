import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "taskapp.db"

print("Database path:", DATABASE_PATH)
print("Database exists:", DATABASE_PATH.exists())

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

print("\nTables:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall())

print("\nUsers:")
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

for user in users:
    print(user)

conn.close()
