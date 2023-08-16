import sqlite3
from type import DbChatItem

conn = sqlite3.connect("./db/spec.db", check_same_thread=False)

cur = conn.cursor()


def init():
    print("checking config")
    print("initialize db")
    print("creating chat db")
    try:
        cur.execute("CREATE TABLE chats(session_id, date, role, message)")
        conn.commit()
        print("Table 'chats' created successfully.")
    except sqlite3.OperationalError:
        print("Table 'chats' already exists.")


def insert_chat(chat: DbChatItem):
    query = "INSERT INTO chats (session_id, date, role, message) VALUES (?, ?, ?, ?)"
    values = (chat.session_id, chat.date, chat.role, chat.message)
    cur.execute(query, values)
    conn.commit()


def get_chat(session_id: str):
    query = "SELECT * FROM chats WHERE session_id=?"
    cur.execute(query, (session_id,))
    res = cur.fetchall()
    return res
