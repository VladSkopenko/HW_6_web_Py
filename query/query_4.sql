SELECT subjects.name_subject
FROM subjects
JOIN teachers ON subjects.master_of_subject = teachers.id
WHERE teachers.name_teacher = 'Марта Петрик';