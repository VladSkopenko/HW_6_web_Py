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
q_2 = """
"""

q_3 = """
"""
q_4 = """
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
q_11 ="""
"""
list_q = []




with sqlite3.connect('test.db') as conn:
    cur = conn.cursor()
    cur.execute()
    rows = cur.fetchall()
    for row in rows:
        print(row)

