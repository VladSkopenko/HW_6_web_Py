SELECT DISTINCT subjects.name_subject, students.name_student, teachers.name_teacher
FROM students
JOIN ratings ON students.id = ratings.id_student
JOIN subjects ON ratings.id_subjects = subjects.id
JOIN teachers ON subjects.master_of_subject = teachers.id
WHERE students.name_student = 'Трохим Тимченко' AND teachers.name_teacher = 'Лілія Редько';
