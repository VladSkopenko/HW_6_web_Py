SELECT subjects.name_subject, teachers.name_teacher, AVG(ratings.grade)
FROM teachers
JOIN subjects ON subjects.master_of_subject = teachers.id
JOIN ratings ON subjects.id = ratings.id_subjects
WHERE teachers.name_teacher = "Лілія Редько"
GROUP BY subjects.name_subject, teachers.name_teacher;