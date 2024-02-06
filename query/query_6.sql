SELECT students.name_student, ratings.grade, subjects.name_subject
FROM students
JOIN groups ON students.group_id = groups.id
JOIN ratings ON students.id = ratings.id_student
JOIN subjects ON ratings.id_subjects = subjects.id
WHERE groups.group_name = 'Учет-22-3' AND subjects.name_subject = 'Фінанси';