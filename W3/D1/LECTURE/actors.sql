-- CREATE TABLE actors(
--  actor_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  age DATE NOT NULL,
--  number_oscars SMALLINT NOT NULL
-- )

-- SELECT * FROM actors

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Matt','Damon','08/10/1970', 5);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES ('George','Clooney','06/05/1961', 2),
-- ('Mia','Goth','10/25/1993', 0),
-- ('Meryl','Streep','06/22/1949', 3);
-- select * from actors
-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- Values ('Daniel','Day-Lewis','04/29/1957','3'),
-- ('Marlon','Brando','04/03/1924', '2'),
-- ('Jack', 'Nicholson','04/22/1937','2');

-- select *from actors

-- select * from actors
-- SELECT * FROM actors WHERE number_oscars >= 3;
-- SELECT first_name, last_name, age, number_oscars, COUNT(*)
-- FROM actors
-- GROUP BY first_name, last_name, age, number_oscars
-- HAVING COUNT(*) > 1;

-- WITH cte AS (
--     SELECT 
--         actor_id,
--         ROW_NUMBER() OVER (PARTITION BY first_name, last_name, age, number_oscars ORDER BY actor_id) AS rn
--     FROM actors
-- )
-- DELETE FROM actors
-- WHERE actor_id IN (
--     SELECT actor_id
--     FROM cte
--     WHERE rn > 1
-- );
select * from actors