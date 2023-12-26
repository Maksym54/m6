from sqlalchemy import func
from sqlalchemy.orm import Session
from models import Student, Grade, Subject, Teacher, Group

def select_2(session, subject_name):
    # Знайти студента із найвищим середнім балом з певного предмета.
    result = (
        session.query(Student, func.avg(Grade.grade).label('avg_grade'))
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.name == subject_name)
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .first()
    )
    return result

def select_3(session, subject_name):
    # Знайти середній бал у групах з певного предмета.
    result = (
        session.query(Group.name, func.avg(Grade.grade).label('avg_grade'))
        .join(Student, Group.id == Student.group_id)
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.name == subject_name)
        .group_by(Group.id)
        .all()
    )
    return result

def select_4(session):
    # Знайти середній бал на потоці (по всій таблиці оцінок).
    result = session.query(func.avg(Grade.grade).label('avg_grade')).scalar()
    return result

def select_5(session, teacher_name):
    # Знайти які курси читає певний викладач.
    result = (
        session.query(Subject.name)
        .join(Teacher, Subject.teacher_id == Teacher.id)
        .filter(Teacher.fullname == teacher_name)
        .distinct()
        .all()
    )
    return result

def select_6(session, group_name):
    # Знайти список студентів у певній групі.
    result = session.query(Student).join(Group, Student.group_id == Group.id).filter(Group.name == group_name).all()
    return result

def select_7(session, group_name, subject_name):
    # Знайти оцінки студентів у окремій групі з певного предмета.
    result = (
        session.query(Student, Grade)
        .join(Group, Student.group_id == Group.id)
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Group.name == group_name, Subject.name == subject_name)
        .all()
    )
    return result

def select_8(session, teacher_name):
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    result = (
        session.query(func.avg(Grade.grade).label('avg_grade'))
        .join(Teacher, Subject.teacher_id == Teacher.id)
        .join(Grade, Subject.id == Grade.subject_id)
        .filter(Teacher.fullname == teacher_name)
        .scalar()
    )
    return result

def select_9(session, student_name):
    # Знайти список курсів, які відвідує студент.
    result = (
        session.query(Subject.name)
        .join(Student, Subject.id == Student.id)
        .filter(Student.fullname == student_name)
        .all()
    )
    return result

def select_10(session, student_name, teacher_name):
    # Список курсів, які певному студенту читає певний викладач.
    result = (
        session.query(Subject.name)
        .join(Student, Subject.id == Student.id)
        .join(Teacher, Subject.teacher_id == Teacher.id)
        .filter(Student.fullname == student_name, Teacher.fullname == teacher_name)
        .all()
    )
    return result