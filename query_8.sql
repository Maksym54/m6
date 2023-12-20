SELECT AVG(grades.grade) AS average_teacher_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.teacher_id = (SELECT id FROM teachers WHERE fullname = 'Bohdan Nnn');
