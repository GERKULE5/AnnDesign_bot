from src.database.db import get_db_conection

def add_user(user_id: int, username: str, name: str, phone: str, description: str) -> bool:
    with get_db_conection() as conn:
        conn.execute("""
            INSERT INTO Users (user_id, username, name, phone, description)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, username, name, phone, description))
        conn.commit()