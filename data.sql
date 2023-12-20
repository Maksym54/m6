-- Додати вчителів
INSERT INTO teachers (fullname) VALUES ('Stpan Ccc');
INSERT INTO teachers (fullname) VALUES ('Anastasiya Ggg');
INSERT INTO teachers (fullname) VALUES ('Bohdan Nnn');

-- Додати предмети
INSERT INTO subjects (name, teacher_id) VALUES ('Math', 1);
INSERT INTO subjects (name, teacher_id) VALUES ('Physics', 2);
INSERT INTO subjects (name, teacher_id) VALUES ('History', 3);

-- Додати групи
INSERT INTO groups (name) VALUES ('Group A');
INSERT INTO groups (name) VALUES ('Group B');

-- Додати студентів
INSERT INTO students (fullname, group_id) VALUES ('Grisha Ddd', 1);
INSERT INTO students (fullname, group_id) VALUES ('Ricardo Fff', 2);
INSERT INTO students (fullname, group_id) VALUES ('Petro Hhh', 1);
INSERT INTO students (fullname, group_id) VALUES ('Danyl Bbb', 2);

-- Додати оцінки студентів за предмети
INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (1, 1, 85, '2023-01-15 00:00:00');
INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (1, 2, 92, '2023-02-01 00:00:00');
INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (2, 1, 78, '2023-01-20 00:00:00');
INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (2, 3, 90, '2023-02-05 00:00:00');
INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (3, 1, 88, '2023-01-18 00:00:00');
INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (3, 2, 34, '2023-01-08 00:00:00');
INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (4, 3, 58, '2023-02-02 00:00:00');
INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (4, 2, 78, '2023-01-30 00:00:00');