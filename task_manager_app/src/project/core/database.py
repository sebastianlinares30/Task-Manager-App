import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "taskapp.db"


def get_connection():
    """
    Creates and returns a connection to the local SQLite database.
    """
    return sqlite3.connect(DATABASE_PATH)