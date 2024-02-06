SELECT students.name_student, groups.group_name
FROM students
JOIN groups ON students.group_id = groups.id
WHERE group_id = 1;