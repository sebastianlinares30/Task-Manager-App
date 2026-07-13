import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "taskapp.db"

# print("Opening the global SQLite database connection...")
# This variable is created ONCE when the app starts up
#_global_connection = sqlite3.connect(DATABASE_PATH, check_same_thread=False)

def get_connection():
    """
    Creates and returns a connection to the local SQLite database.
    """
    return sqlite3.connect(DATABASE_PATH)
    # return _global_connection
