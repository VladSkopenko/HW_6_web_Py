SELECT subjects.name_subject, students.name_student
FROM students
JOIN ratings ON students.id = ratings.id_student
JOIN subjects ON ratings.id_subjects = subjects.id
WHERE students.name_student = 'Мілена Свистун';