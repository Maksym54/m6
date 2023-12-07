import logging
from sqlite3 import DatabaseError
from faker import Faker
import random
import psycopg2

fake = Faker()


conn = psycopg2.connect(host="localhost", database="m6", user="SQLite", password="123456")
cur = conn.cursor()


for _ in range(3):
    cur.execute("INSERT INTO groups (name) VALUES (%s) RETURNING group_id", (fake.word(),))
    group_id = cur.fetchone()[0]


for _ in range(3):
    cur.execute("INSERT INTO teachers (fullname) VALUES (%s) RETURNING teacher_id",
                (fake.name()))
    teacher_id = cur.fetchone()[0]

for teacher_id in range(1, 4):
    for _ in range(2):
        cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)", (fake.word(), teacher_id))


for _ in range(30):
    cur.execute("INSERT INTO students (fullname, group_id) VALUES (%s, %s) RETURNING student_id",
                (fake.full_name(), random.choice(range(1, 4))))
    student_id = cur.fetchone()[0]

    for subject_id in range(1, 7):
        for _ in range(3):
            cur.execute("INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (%s, %s, %s, %s)",
                        (student_id, subject_id, random.randint(0, 100), fake.date_this_decade()))

conn.commit()

try:
    conn.commit()
except DatabaseError as e:
    logging.error(e)
    conn.rollback()
finally:
    cur.close()
    conn.close()