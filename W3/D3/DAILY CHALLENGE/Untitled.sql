-- CREATE TABLE Book (
-- 	book_id SERIAL PRIMARY KEY, 
-- 	title 	VARCHAR(50) NOT NULL, 
-- 	author VARCHAR(50) NOT NULL
-- );
-- INSERT INTO Book (title, author) VALUES ('Alice In Wonderland', 'Lewis Carroll');
-- INSERT INTO Book (title, author) VALUES ('Harry Potter', 'J.K Rowling');
-- INSERT INTO Book (title, author) VALUES ('To kill a mockingbird', 'Harper Lee');

-- CREATE TABLE Student (
-- 	student_id SERIAL PRIMARY KEY, 
-- 	name VARCHAR(50) NOT NULL UNIQUE, 
-- 	age INT CHECK (age<=15) 
-- );

-- INSERT INTO Student (name, age) VALUES ('John', 12);
-- INSERT INTO Student (name, age) VALUES ('Lera', 11);
-- INSERT INTO Student (name, age) VALUES ('Patrick', 10);
-- INSERT INTO Student (name, age) VALUES ('Bob', 14);

-- CREATE TABLE Library (
--     book_fk_id INT,
--     student_fk_id INT,
--     borrowed_date DATE,
--     PRIMARY KEY (book_fk_id, student_fk_id),
--     FOREIGN KEY (book_fk_id) REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
--     FOREIGN KEY (student_fk_id) REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
-- );


-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES
--     ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM Student WHERE name = 'John'), '2022-02-15'),
--     ((SELECT book_id FROM Book WHERE title = 'To Kill a Mockingbird'), (SELECT student_id FROM Student WHERE name = 'Bob'), '2021-03-03'),
--     ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM Student WHERE name = 'Lera'), '2021-05-23'),
--     ((SELECT book_id FROM Book WHERE title = 'Harry Potter'), (SELECT student_id FROM Student WHERE name = 'Bob'), '2021-08-12');

-- SELECT * FROM Library;

-- SELECT s.name AS student_name, b.title AS book_title, l.borrowed_date
-- FROM Library l
-- JOIN Book b ON l.book_fk_id = b.book_id
-- JOIN Student s ON l.student_fk_id = s.student_id;

-- SELECT AVG(s.age) AS avg_age
-- FROM Library l
-- JOIN Book b ON l.book_fk_id = b.book_id
-- JOIN Student s ON l.student_fk_id = s.student_id
-- WHERE b.title = 'Alice In Wonderland';

-- DELETE FROM Student WHERE name = 'John';
-- When we delete a student like "John" from the Student table, the ON DELETE CASCADE 
-- rule automatically deletes all related records from the Library table where John's ID is referenced.

