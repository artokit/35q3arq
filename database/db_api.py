import os.path
import sqlite3
from sqlite3 import IntegrityError

connect = sqlite3.connect(os.path.join(os.path.dirname(__file__), "db.sqlite"))
cursor = connect.cursor()


def add_user(user_id: int, username: str, utm: str):
    try:
        cursor.execute("INSERT INTO USERS VALUES (?,?,?)", (user_id, username, utm))
        connect.commit()
    except IntegrityError:
        pass


def get_user(user_id: int):
    return cursor.execute("SELECT * FROM USERS WHERE id = ? ", (user_id,)).fetchone()
