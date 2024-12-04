import sqlite3
from sqlite3 import DatabaseError


def create_db():
    with open('task_management_table_creation.sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect('task_management.db') as con:
        cur = con.cursor()
        try:
            cur.executescript(sql)
            con.commit()
        except DatabaseError as e:
            print(e)
            con.rollback()
        finally:
            cur.close()


if __name__ == "__main__":
    create_db()
