import sqlite3
from datetime import datetime, date, timedelta
from faker import Faker
from random import randint
import logging

subject = ['Математика', 'Банківська справа', 'Фінанси', 'Право', 'Статистика', 'Загальна економічна теорія',
           'Програмування']
groups = ['Феф-22-1', 'Феоп-22-2', 'Учет-22-3']

NUMBER_TEACHERS = randint(5, 8)
NUMBER_STUDENTS = randint(30, 50)

fake = Faker('uk_UA')

connect = sqlite3.connect('test.db')
cur = connect.cursor()


def seed_teachers():
    teachers = [fake.name() for _ in range(NUMBER_TEACHERS)]
    sql = "INSERT INTO teachers(name_teacher) VALUES(?);"
    cur.executemany(sql, zip(teachers, ))


def seed_subject():
    sql = "INSERT INTO subjects(name_subject, master_of_subject) VALUES(?, ?);"
    cur.executemany(sql, zip(subject, iter(randint(1, NUMBER_TEACHERS) for _ in range(len(subject)))))


def seed_groups():
    sql = "INSERT INTO groups(group_name) VALUES(?);"
    cur.executemany(sql, zip(groups, ))


def seed_students():
    students = [fake.name() for _ in range(NUMBER_STUDENTS)]
    sql = "INSERT INTO students(name_student, group_id) VALUES(?, ?);"
    cur.executemany(sql, zip(students, iter(randint(1, len(groups)) for _ in range(len(students)))))


def get_list_dates(start: date, end: date):
    result = []
    current_date = start
    while current_date <= end:
        if current_date.isoweekday() < 6:
            result.append(current_date)
        current_date += timedelta(1)
    return result


def seed_rating():
    start_date = datetime.strptime('2023-05-31', '%Y-%m-%d')
    end_date = datetime.strptime('2024-02-06', '%Y-%m-%d')
    sql = "INSERT INTO ratings(id_subjects, id_student, grade, when_received) VALUES(?, ?, ?, ?);"
    list_dates = get_list_dates(start_date, end_date)
    grades = []
    for day in list_dates:
        random_discipline = randint(1, len(subject))
        random_students = [randint(1, NUMBER_STUDENTS) for _ in range(5)]
        for student in random_students:
            grades.append((random_discipline, student, randint(1, 100), day.date()))
    cur.executemany(sql, grades)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s%(message)s")
    try:
        seed_teachers()
        seed_subject()
        seed_groups()
        seed_students()
        seed_rating()
        connect.commit()
    except sqlite3.Error as error:
        logging.error(error)
    finally:
        connect.close()
