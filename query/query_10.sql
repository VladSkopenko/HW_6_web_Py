SELECT subjects.name_subject, students.name_student, teachers.name_teacher, AVG(r.grade) AS average_grade
FROM ratings r
JOIN subjects ON r.id_subjects = subjects.id
JOIN teachers ON subjects.master_of_subject = teachers.id
JOIN students ON r.id_student = students.id
WHERE teachers.name_teacher = 'Лілія Редько' AND students.name_student = 'Трохим Тимченко'
GROUP BY subjects.name_subject, students.name_student, teachers.name_teacher;
