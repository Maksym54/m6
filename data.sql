-- Додати вчителів
INSERT INTO teachers (fullname) VALUES ('Stpan');
INSERT INTO teachers (fullname) VALUES ('Anastasiya');
INSERT INTO teachers (fullname) VALUES ('Bohdan');

-- Додати предмети
INSERT INTO subjects (name, teacher_id) VALUES ('Math', 1);
INSERT INTO subjects (name, teacher_id) VALUES ('Physics', 2);
INSERT INTO subjects (name, teacher_id) VALUES ('History', 3);

-- Додати групи
INSERT INTO groups (name) VALUES ('Group A');
INSERT INTO groups (name) VALUES ('Group B');

-- Додати студентів
INSERT INTO students (fullname, group_id) VALUES ('Grisha', 1);
INSERT INTO students (fullname, group_id) VALUES ('Ricardo', 2);
INSERT INTO students (fullname, group_id) VALUES ('Petro', 1);

-- Додати оцінки студентів за предмети
INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (1, 1, 85, '2023-01-15 00:00:00');
INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (1, 2, 92, '2023-02-01 00:00:00');
INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (2, 1, 78, '2023-01-20 00:00:00');
INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (2, 3, 90, '2023-02-05 00:00:00');
INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (3, 1, 88, '2023-01-18 00:00:00');
