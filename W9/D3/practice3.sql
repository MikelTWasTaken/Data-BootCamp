CREATE TABLE practice.sample_data (id INT, value VARCHAR(50));
INSERT INTO practice.sample_data (id, value) VALUES (1, 'apple'), (2, 'Apple'), (3, 'APPLE'), (4, NULL);

SELECT *
FROM practice.sample_data
WHERE id IS NULL OR value is NULL;

SELECT COALESCE(value, 'Apple') FROM practice.sample_data;
UPDATE practice.sample_data
SET value = 'Apple'
WHERE value IS NULL;

select value, INITCAP(value)
from practice.sample_data
UPDATE practice.sample_data
SET value = INITCAP(value);

select * from practice.sample_data