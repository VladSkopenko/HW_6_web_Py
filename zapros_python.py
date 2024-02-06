import sqlite3

q_0 = """SELECT s.id, s.name_student, AVG(r.grade) AS average_grade
FROM students s
JOIN ratings r ON s.id = r.id_student
GROUP BY s.id, s.name_student
ORDER BY average_grade DESC
LIMIT 5;
"""
q_1 = """SELECT s.id, s.name_student, AVG(r.grade) AS average_grade
FROM students s
JOIN ratings r ON s.id = r.id_student
JOIN subjects sb ON r.id_subjects = sb.id
WHERE sb.name_subject = 'Математика'
GROUP BY s.id, s.name_student
ORDER BY average_grade DESC
LIMIT 1;
"""
q_2 = """SELECT g.group_name, AVG(r.grade) AS average_grade
FROM students s
JOIN groups g ON s.group_id = g.id
JOIN ratings r ON s.id = r.id_student
JOIN subjects sub ON r.id_subjects = sub.id
WHERE sub.name_subject = 'Математика'
GROUP BY g.group_name;

"""

q_3 = """SELECT AVG(grade) AS average_grade
FROM ratings;
"""
q_4 = """SELECT subjects.name_subject
FROM subjects
JOIN teachers ON subjects.master_of_subject = teachers.id
WHERE teachers.name_teacher = 'Марта Петрик';
"""
q_5 = """
"""
q_6 = """
"""
q_7 = """
"""
q_8 = """
"""
q_9 = """
"""
q_10 = """
"""
q_11 = """
"""
for_test = q_4

with sqlite3.connect('test.db') as conn:
    cur = conn.cursor()
    cur.execute(for_test)
    rows = cur.fetchall()
    for row in rows:
        print(row)
