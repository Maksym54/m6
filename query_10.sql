SELECT DISTINCT subjects.name
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.id
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
WHERE students.fullname = 'Grisha Ddd'
  AND teachers.fullname = 'Anastasiya Ggg';
