import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent.parent / 'src' / 'database' / 'bot_db'

def get_db_conection():
    conn = sqlite3.connect(DB_PATH)
    return conn

def init_db():
    with get_db_conection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                username TEXT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                description TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
        conn.commit()