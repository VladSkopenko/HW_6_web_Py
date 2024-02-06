SELECT g.group_name, sub.name_subject, AVG(r.grade) AS average_grade
FROM students s
JOIN groups g ON s.group_id = g.id
JOIN ratings r ON s.id = r.id_student
JOIN subjects sub ON r.id_subjects = sub.id
WHERE sub.name_subject = 'Математика'
GROUP BY g.group_name, sub.name_subject;
