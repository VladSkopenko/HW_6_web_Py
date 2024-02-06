-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    name_student VARCHAR(35) NOT NULL,
    group_id INT,
    FOREIGN KEY (group_id) REFERENCES groups(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE

);

-- Table: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    group_name VARCHAR(230) UNIQUE NOT NULL
);

-- Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    name_teacher VARCHAR(30) NOT NULL
);

-- Table: subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    name_subject VARCHAR(30) UNIQUE NOT NULL,
    master_of_subject INT,
    FOREIGN KEY (master_of_subject) REFERENCES teachers(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Table: ratings
DROP TABLE IF EXISTS ratings;
CREATE TABLE ratings(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    when_received DATE NOT NULL,
    id_student INT REFERENCES students(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    id_subjects INT REFERENCES subjects(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    grade INTEGER

);
