import sqlite3

DB_NAME = "clear7.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS settings (
        chat_id INTEGER PRIMARY KEY,
        auto_delete INTEGER DEFAULT 1,
        delete_time INTEGER DEFAULT 10
    )
    """)

    conn.commit()
    conn.close()
