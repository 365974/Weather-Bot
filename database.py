import sqlite3

def init_db():
    conn = sqlite3.connect("history.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            user_id INTEGER,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_message(user_id, message):
    conn = sqlite3.connect("history.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (user_id, message) VALUES (?, ?)", (user_id, message))
    conn.commit()
    conn.close()

def get_history(user_id):
    conn = sqlite3.connect("history.db")
    cur = conn.cursor()
    cur.execute("SELECT message FROM messages WHERE user_id=?", (user_id,))
    messages = cur.fetchall()
    conn.close()
    return [msg[0] for msg in messages]
