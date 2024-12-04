from sqlite3 import DatabaseError

import faker
from random import randint
import sqlite3

NUMBER_OF_USERS = 10
NUMBER_OF_TASKS = 100
STATUSES = [('new',), ('in progress',), ('completed',), ('not solved',)]


def generate_fake_data(number_of_users, number_of_tasks) -> tuple:
    fake_users = []
    fake_tasks = []

    fake_data = faker.Faker()

    for _ in range(number_of_users):
        fake_users.append((fake_data.name(), fake_data.email()))

    for _ in range(number_of_tasks):
        fake_tasks.append((fake_data.word(), fake_data.text()))

    return fake_users, fake_tasks


def prepare_data(users, tasks, statuses) -> tuple:
    for_statuses = []

    for status in statuses:
        for_statuses.append(status)

    for_users = []

    for user in users:
        for_users.append((*user, ))

    for_tasks = []

    for task in tasks:
        for_tasks.append((*task, randint(1, len(STATUSES)), randint(1, NUMBER_OF_USERS)))

    return for_users, for_tasks, for_statuses


def insert_data_to_db(users, tasks, statuses) -> None:
    with sqlite3.connect('task_management.db') as con:
        cur = con.cursor()

        try:
            sql_users = """INSERT INTO users(fullname, email) 
            VALUES (?, ?)"""
            cur.executemany(sql_users, users)

            sql_status = """INSERT INTO status(name)
            VALUES (?)"""
            cur.executemany(sql_status, statuses)

            sql_tasks = """INSERT INTO tasks(title, description, status_id, user_id)
            VALUES (?, ?, ?, ?)"""
            cur.executemany(sql_tasks, tasks)

            con.commit()

        except DatabaseError as e:
            print(e)
            con.rollback()

        finally:
            cur.close()


if __name__ == "__main__":
    users, tasks, statuses = prepare_data(
        *generate_fake_data(number_of_users=NUMBER_OF_USERS, number_of_tasks=NUMBER_OF_TASKS), STATUSES
    )
    insert_data_to_db(users=users, tasks=tasks, statuses=statuses)
