import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('task_management.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql_1 = """SELECT t.id, t.title, t.description, t.user_id
FROM tasks t
WHERE t.user_id = 1
ORDER BY t.id;
"""

sql_2 = """SELECT t.id, t.title, t.description, t.user_id
FROM tasks t
JOIN status s ON t.status_id = s.id
WHERE s.name = 'not solved';
"""

sql_3 = """UPDATE tasks
SET status_id = (
    SELECT id
    FROM status
    WHERE name = 'not solved'
    )
WHERE id = 2;
"""

sql_4 = """SELECT *
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
WHERE t.id is NULL;
"""

sql_5 = """INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('Newly added task', 'You have to do a lot of things', (SELECT id FROM status WHERE name = 'new'), 12);
"""

sql_6 = """SELECT *
FROM tasks t
JOIN status s ON s.id = t.status_id
WHERE s.name != 'completed';
"""

sql_7 = """DELETE FROM tasks
WHERE id = 101;
"""

sql_8 = """SELECT *
FROM users u
WHERE u.email LIKE '%.com'
ORDER BY u.id;
"""

sql_9 = """UPDATE users
SET fullname = 'Dean L Jones'
WHERE id = 12;
"""

sql_10 = """SELECT COUNT(t.status_id), s.name
FROM tasks t
JOIN status s ON s.id = t.status_id
GROUP BY s.name;
"""

sql_11 = """SELECT *
FROM tasks t
JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%.com'
ORDER BY t.title;
"""

sql_12 = """
SELECT *
FROM tasks t
WHERE t.description is NULL or t.description = '';
"""

sql_13 = """SELECT u.fullname AS user, t.title, t.description
FROM users u
JOIN tasks t ON u.id = t.user_id
JOIN status s ON s.id = t.status_id
WHERE s.name = 'in progress';
"""

sql_14 = """SELECT u.fullname, COUNT(t.user_id)
FROM users u 
JOIN tasks t ON u.id = t.user_id
GROUP BY u.fullname;
"""


if __name__ == "__main__":
    print(execute_query(sql_14))
