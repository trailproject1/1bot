import sqlite3

DB_NAME = "clear7.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings(
            chat_id INTEGER PRIMARY KEY,
            auto_delete INTEGER DEFAULT 1,
            delete_time INTEGER DEFAULT 10
        )
    """)

    conn.commit()
    conn.close()


def create_chat(chat_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO settings(chat_id)
        VALUES(?)
    """, (chat_id,))

    conn.commit()
    conn.close()


def get_settings(chat_id):
    create_chat(chat_id)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT auto_delete, delete_time
        FROM settings
        WHERE chat_id=?
    """, (chat_id,))

    result = cursor.fetchone()

    conn.close()

    return result


def set_auto(chat_id, value):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE settings
        SET auto_delete=?
        WHERE chat_id=?
    """, (value, chat_id))

    conn.commit()
    conn.close()


def set_time(chat_id, minutes):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE settings
        SET delete_time=?
        WHERE chat_id=?
    """, (minutes, chat_id))

    conn.commit()
    conn.close()
