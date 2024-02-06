SELECT groups.group_name,
       subjects.name_subject,
       ratings.grade,
       ratings.when_received,
       students.name_student
FROM subjects
JOIN groups ON groups.id = 1
JOIN ratings ON subjects.id = 1
JOIN students ON students.id = ratings.id_student
WHERE ratings.when_received = (
    SELECT MAX(r.when_received)
    FROM ratings r
    WHERE r.id_subjects = subjects.id
);
