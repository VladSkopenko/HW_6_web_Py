import sqlite3

q_0 = """SELECT s.id, s.name_student, AVG(r.grade) AS average_grade
FROM students s
JOIN ratings r ON s.id = r.id_student
GROUP BY s.id, s.name_student
ORDER BY average_grade DESC
LIMIT 5;
"""
q_1 = """SELECT s.id, s.name_student, sb.name_subject, AVG(r.grade) AS average_grade 
FROM students s
JOIN ratings r ON s.id = r.id_student
JOIN subjects sb ON r.id_subjects = sb.id
WHERE sb.name_subject = 'Математика'
GROUP BY s.id, s.name_student, sb.name_subject
ORDER BY average_grade DESC
LIMIT 1;

"""
q_2 = """SELECT g.group_name, sub.name_subject, AVG(r.grade) AS average_grade
FROM students s
JOIN groups g ON s.group_id = g.id
JOIN ratings r ON s.id = r.id_student
JOIN subjects sub ON r.id_subjects = sub.id
WHERE sub.name_subject = 'Математика'
GROUP BY g.group_name, sub.name_subject;
"""

q_3 = """SELECT AVG(grade) AS average_grade
FROM ratings;
"""
q_4 = """SELECT subjects.name_subject, teachers.name_teacher
FROM subjects
JOIN teachers ON subjects.master_of_subject = teachers.id
WHERE teachers.name_teacher = 'Марта Петрик';
"""
q_5 = """SELECT students.name_student, groups.group_name
FROM students
JOIN groups ON students.group_id = groups.id
WHERE group_id = 1;
"""

q_6 = """SELECT students.name_student, ratings.grade, subjects.name_subject
FROM students
JOIN groups ON students.group_id = groups.id
JOIN ratings ON students.id = ratings.id_student
JOIN subjects ON ratings.id_subjects = subjects.id
WHERE groups.group_name = 'Учет-22-3' AND subjects.name_subject = 'Фінанси';
"""
q_7 = """SELECT subjects.name_subject, teachers.name_teacher, AVG(ratings.grade)
FROM teachers
JOIN subjects ON subjects.master_of_subject = teachers.id
JOIN ratings ON subjects.id = ratings.id_subjects
WHERE teachers.name_teacher = "Лілія Редько"
GROUP BY subjects.name_subject, teachers.name_teacher;
"""
q_8 = """SELECT subjects.name_subject, students.name_student
FROM students 
JOIN ratings ON students.id = ratings.id_student
JOIN subjects ON ratings.id_subjects = subjects.id
WHERE students.name_student = 'Мілена Свистун';
"""
q_9 = """SELECT DISTINCT subjects.name_subject, students.name_student, teachers.name_teacher
FROM students
JOIN ratings ON students.id = ratings.id_student
JOIN subjects ON ratings.id_subjects = subjects.id
JOIN teachers ON subjects.master_of_subject = teachers.id
WHERE students.name_student = 'Трохим Тимченко' AND teachers.name_teacher = 'Лілія Редько';
"""
q_10 = """SELECT subjects.name_subject, students.name_student, teachers.name_teacher, AVG(r.grade) AS average_grade
FROM ratings r
JOIN subjects ON r.id_subjects = subjects.id
JOIN teachers ON subjects.master_of_subject = teachers.id
JOIN students ON r.id_student = students.id
WHERE teachers.name_teacher = 'Лілія Редько' AND students.name_student = 'Трохим Тимченко'
GROUP BY subjects.name_subject, students.name_student, teachers.name_teacher;


"""
q_11 = """SELECT groups.group_name, 
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

"""
for_test = q_11

with sqlite3.connect('test.db') as conn:
    cur = conn.cursor()
    cur.execute(for_test)
    rows = cur.fetchall()
    for row in rows:
        print(row)
