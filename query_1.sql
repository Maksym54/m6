SELECT students.id, students.fullname, AVG(grades.grade) as average_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.id, students.fullname
ORDER BY average_grade DESC
LIMIT 5;
