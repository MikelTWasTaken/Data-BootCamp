-- SELECT * from actors
-- SELECT AVG(number_oscars) as avg_oscars from actors;
-- SELECT count(first_name) as total_actors from actors;
-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Matt','Ross','03/01/1970', 0);

-- SELECT * FROM actors;

-- SELECT DISTINCT first_name FROM actors ORDER BY first_name DESC;
-- SELECT * FROM actors WHERE age between '1961-01-01' and '1962-01-01';
-- SELECT * FROM actors WHERE first_name in ('Matt','Lea','Davis');
-- INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES('George','Clooney','06/05/1961 ', 1);
-- SELECT first_name, last_name, sum(number_oscars) FROM actors GROUP BY first_name, last_name;
-- SELECT first_name, last_name, sum(number_oscars) FROM actors GROUP BY first_name, last_name 
-- ORDER BY min(number_oscars);
-- 
-- CREATE TABLE movies(
-- movie_id SERIAL,
-- movie_title VARCHAR (50) NOT NULL,
-- movie_story TEXT,
-- actor_playing_id INTEGER,
-- PRIMARY KEY (movie_id),
-- FOREIGN KEY (actor_playing_id) REFERENCES actors (actor_id)
-- );

-- INSERT INTO movies (movie_title, movie_story, actor_playing_id) VALUES
--     ( 'Good Will Hunting', 
--     'Written by Affleck and Damon, the film follows 20-year-old South Boston janitor Will Hunting',
--     (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon')),
--     ( 'Oceans Eleven', 
-- --     'American heist film directed by Steven Soderbergh and written by Ted Griffin.', 
--     (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon'));

-- CREATE TABLE producers(
-- producer_id SERIAL,
-- producer_name VARCHAR(100) NOT NULL,
-- producer_lastname VARCHAR(100) NOT NULL,
-- movie_producer_id INTEGER,
-- PRIMARY KEY (producer_id),
-- FOREIGN KEY (movie_producer_id) REFERENCES movies(movie_id))

-- INSERT INTO producers (producer_name, producer_lastname, movie_producer_id) 
-- VALUES ( 'Lawrence', 'Bender',(SELECT movie_id from movies WHERE movie_title = 'Good Will Hunting'))

-- CREATE TABLE Countries (
--     Country_id SERIAL,
--     Country_name VARCHAR(100) NOT NULL,
--     PRIMARY KEY (Country_id)
-- );
-- INSERT INTO Countries (Country_name)
-- VALUES ('United States'),
--        ('Canada'),
--        ('Mexico'
-- );

-- Select
-- 	producers.producer_name, producers.producer_lastname, movies.movie_title
-- From 
-- 	producers
-- Inner Join 
-- 	movies
-- ON producers.movie_producer_id = movies.movie_id



-- SELECT actors.first_name, countries.country_name
-- FROM actors
-- LEFT OUTER JOIN countries
-- ON actors.actor_id = countries.country_id; 

-- SELECT actors.first_name, countries.country_name
-- FROM countries
-- RIGHT OUTER JOIN actors
-- ON countries.country_id = actors.actor_id;

-- SELECT actors.first_name, countries.country_name
-- FROM countries
-- INNER JOIN actors
-- ON countries.country_id = actors.actor_id;

-- SELECT actors.first_name, countries.country_name
-- FROM countries
-- FULL OUTER JOIN actors
-- ON countries.country_id = actors.actor_id;


