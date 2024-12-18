-- PART 1

-- Get a list of all the languages, from the language table.
-- SELECT * FROM public.language
-- ORDER BY language_id ASC 

-- Get a list of all films joined with their languages – 
-- select the following details : film title, description, and language name.
-- SELECT 
--     f.title AS film_title,
--     f.description,
--     l.name AS language_name
-- FROM 
--     film f
-- JOIN 
--     language l
-- ON 
--     f.language_id = l.language_id;

-- Get all languages, even if there are no films in those languages – 
-- select the following details : film title, description, and language name.

-- SELECT 
--     f.title AS film_title,
--     f.description,
--     l.name AS language_name
-- FROM 
--     language l
-- LEFT JOIN 
--     film f
-- ON 
--     l.language_id = f.language_id;

-- Create a new table called new_film with the following columns : 
-- id, name. Add some new films to the table.
-- CREATE TABLE new_film (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL
-- );

-- CREATE TABLE customer_review (
--     review_id SERIAL PRIMARY KEY,
--     film_id INT NOT NULL,
--     language_id INT NOT NULL,
--     title VARCHAR(255) NOT NULL,
--     score SMALLINT NOT NULL CHECK (score BETWEEN 1 AND 10),
--     review_text TEXT,
--     last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,
--     FOREIGN KEY (language_id) REFERENCES language(language_id) ON DELETE CASCADE
-- );

-- INSERT INTO customer_review (id, language_id, title, score, review_text)
-- VALUES (1, 2, 'Great Movie', 8, 'I really enjoyed this film!');

-- PART 2

-- UPDATE film
-- SET language_id = (
--     SELECT language_id
--     FROM language
--     WHERE name = 'Italian'
-- )
-- WHERE film_id = 5;

-- Which foreign keys (references) are defined for the customer table? 
-- How does this affect the way in which we INSERT into the customer table?
-- address_id is the foreign key, Foreign keys create a relationship between tables and enforce referential integrity. 

-- DROP TABLE customer_review;

-- SELECT COUNT(*) AS outstanding_rentals
-- FROM rental
-- WHERE return_date IS NULL;

-- SELECT 
--     f.title,
--     f.replacement_cost AS price,
--     r.rental_date
-- FROM rental r
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- WHERE r.return_date IS NULL
-- ORDER BY f.replacement_cost DESC
-- LIMIT 30;

-- SELECT f.title, f.description
-- FROM film f
-- JOIN film_actor fa ON f.film_id = fa.film_id
-- JOIN actor a ON fa.actor_id = a.actor_id
-- WHERE a.first_name = 'Penelope' AND a.last_name = 'Monroe'
--   AND f.description ILIKE '%sumo%';

-- SELECT f.title, f.description, f.length, f.rating
-- FROM film f
-- WHERE f.rating = 'R'
--   AND f.length < 60
--   AND f.description ILIKE '%documentary%';

-- SELECT f.title, r.rental_date, r.return_date, p.amount
-- FROM rental r
-- JOIN payment p ON r.rental_id = p.rental_id
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- JOIN customer c ON r.customer_id = c.customer_id
-- WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
--   AND p.amount > 4.00
--   AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

-- SELECT f.title, f.description, f.replacement_cost
-- FROM rental r
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- JOIN customer c ON r.customer_id = c.customer_id
-- WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
--   AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
-- ORDER BY f.replacement_cost DESC
-- LIMIT 1;


