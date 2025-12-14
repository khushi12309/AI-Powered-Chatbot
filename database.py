import sqlite3

conn = sqlite3.connect("chat.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chatlog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    bot TEXT
)
""")
conn.commit()

def save_chat(user, bot):
    cursor.execute("INSERT INTO chatlog (user, bot) VALUES (?, ?)", (user, bot))
    conn.commit()
