SELECT s.id, s.name_student, sb.name_subject, AVG(r.grade) AS average_grade
FROM students s
JOIN ratings r ON s.id = r.id_student
JOIN subjects sb ON r.id_subjects = sb.id
WHERE sb.name_subject = 'Математика'
GROUP BY s.id, s.name_student, sb.name_subject
ORDER BY average_grade DESC
LIMIT 1;
