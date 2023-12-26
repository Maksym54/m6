from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Base, Group, Student, Teacher, Subject, Grade
from datetime import date, timedelta
import random

fake = Faker()
engine = create_engine('postgresql://postgres:mysecretpassword@localhost:5432/mydatabase')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def seed_data():
    groups = [Group(name=fake.word()) for _ in range(3)]
    session.add_all(groups)
    session.commit()

    teachers = [Teacher(fullname=fake.name()) for _ in range(5)]
    session.add_all(teachers)
    session.commit()

    subjects = [Subject(name=fake.word(), teacher=random.choice(teachers)) for _ in range(8)]
    session.add_all(subjects)
    session.commit()

    students = [Student(fullname=fake.name(), group=random.choice(groups)) for _ in range(50)]
    session.add_all(students)
    session.commit()

    for student in students:
        for subject in subjects:
            grade = random.randint(60, 100)
            grade_date = date.today() - timedelta(days=random.randint(1, 365))
            session.add(Grade(student=student, subject=subject, grade=grade, grade_date=grade_date))

    session.commit()

if __name__ == '__main__':
    seed_data()
