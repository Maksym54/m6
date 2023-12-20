SELECT students.fullname
FROM students
WHERE students.group_id = (SELECT id FROM groups WHERE name = 'Group A');
