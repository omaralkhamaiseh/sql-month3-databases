CREATE TABLE students(
    student_id Integer PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    major TEXT NOT NULL
);
-----------------------------
CREATE TABLE courses(
    course_id Integer PRIMARY KEY,
    course_name TEXT NOT NULL,
    credits Integer NOT NULL CHECK(credits>0),
    department TEXT NOT NULL
);
---------------------
CREATE TABLE enrollments(
    enrollment_id Integer PRIMARY KEY,
    student_id Integer NOT NULL,
    course_id Integer NOT NULL,
    enrollment_date TEXT NOT NULL,
    FOREIGN KEY(student_id)
        REFERENCES students(student_id),
    FOREIGN KEY(course_id)
        REFERENCES courses(course_id)
);
---------------------
INSERT INTO students(student_id,name,email,major)
VALUES
    (1,'Ahmad','ahmad@gmail.com','Software Engineer'),
    (2,'Omar','omar@gmail.com','Computer Science'),
    (3,'Lina','lina@gmail.com','Cybersecurity'),
    (4,'Sara','sara@gmail.com','Software Engineer');
    ----------------------------
INSERT INTO courses(course_id,course_name,credits,department)
VALUES
    (101,'Python Programming',3,'Computer Science'),
    (102,'Database Systems',3,'Software Engineer'),
    (103,'Java Programming',4,'Software Engineer'),
    (104,'Network Security',3,'Cybersecurity'),
    (105,'Artificial Intelligence',4,'Computer Science');
    -----------------------------
INSERT INTO enrollments(enrollment_id,student_id,course_id,enrollment_date)
VALUES
    (1, 1, 101, '2026-11-15'),
    (2, 1, 102, '2026-11-15'),
    (3, 2, 103, '2026-11-15'),
    (4, 2, 105, '2026-11-15'),
    (5, 3, 104, '2026-11-15'),
    (6, 4, 102, '2026-11-15');
    ------------------------
SELECT s.name,e.course_id
From students AS s
INNER JOIN enrollments AS e
ON s.student_id=e.student_id;
--------------------
SELECT s.name,c.course_name
FROM students AS s
INNER JOIN enrollments AS e
ON s.student_id=e.student_id
INNER JOIN courses AS c 
ON e.course_id=c.course_id;
-------------------
SELECT s.name,c.course_name
FROM students AS s 
INNER JOIN enrollments AS e
ON s.student_id=e.student_id
INNER JOIN courses AS c
ON e.course_id=c.course_id
WHERE c.course_name='Database Systems';
--------------------------------
SELECT s.name,e.course_id
FROM students AS s 
LEFT JOIN enrollments AS e
ON s.student_id=e.student_id;
------------------------------
INSERT INTO students(student_id,name,email,major)
VALUES
    (5,'Khaled','khaled@gmail.com','Computer Science');
--------------------------------------
SELECT s.name,e.course_id
FROM students AS s 
LEFT JOIN enrollments AS e
ON s.student_id=e.student_id
WHERE e.course_id IS NULL;
--------------------------------
SELECT c.course_name, COUNT(e.enrollment_id) AS total_students
FROM courses AS c 
LEFT JOIN enrollments AS e
ON c.course_id=e.course_id
GROUP BY c.course_name,c.course_id;
--------------------------------
SELECT c.course_name,Count(e.enrollment_id) AS total_students
FROM courses AS c 
LEFT JOIN enrollments AS e
ON c.course_id=e.course_id
GROUP BY c.course_name,c.course_id
ORDER BY total_students DESC;
----------------------------------
SELECT s.name,COUNT(e.course_id) AS total_courses
FROM students AS s
INNER JOIN enrollments AS e
ON s.student_id=e.student_id
GROUP BY s.name,s.student_id
Having COUNT(e.course_id) > 1;
------------------------------------
INSERT INTO courses (course_id, course_name, credits, department)
VALUES (106, 'Cloud Computing', 3, 'Computer Science');
------------------------------------------------------
SELECT c.course_name
FROM courses AS c 
LEFT JOIN enrollments AS e
ON c.course_id=e.course_id
WHERE e.enrollment IS NULL;
----------------------------------
SELECT course_name,credits
FROM courses 
WHERE credits > 3;
-------------------
SELECT course_name,credits
FROM courses 
WHERE credits > 3
ORDER BY course_name ASC;
----------------------
SELECT s.name,COUNT(e.enrollment_id) AS total_courses
FROM students AS s 
LEFT JOIN enrollments AS e
ON s.student_id=e.student_id
GROUP BY s.student_id, s.name
ORDER BY total_courses DESC;