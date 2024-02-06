SELECT s.id, s.name_student, AVG(r.grade) AS average_grade
FROM students s
JOIN ratings r ON s.id = r.id_student
GROUP BY s.id, s.name_student
ORDER BY average_grade DESC
LIMIT 5;
