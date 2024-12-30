-- 🌟 Exercise 2: Advanced Data Manipulation and Optimization
-- Task 1: Update the heights of competitors based on the average height of 
-- competitors from the same region. Use a correlated subquery within the UPDATE statement.

UPDATE olympics.games_competitor gc
SET age = (
    SELECT AVG(p.height)
    FROM olympics.person p
    JOIN olympics.person_region pr ON p.id = pr.person_id
    WHERE pr.region_id = (
        SELECT pr2.region_id
        FROM olympics.person_region pr2
        WHERE pr2.person_id = gc.person_id
    )
);


-- Task 2: Insert new records into a temporary table for competitors who 
-- participated in more than one event in the same games and list their total number of events 
-- participated. Use nested subqueries for filtering.
CREATE TEMPORARY TABLE temp_competitor_events (
    competitor_id INT,
    total_events INT
);
INSERT INTO temp_competitor_events (competitor_id, total_events)
SELECT gc.person_id, COUNT(ce.event_id) AS total_events
FROM olympics.games_competitor gc
JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
WHERE gc.id IN (
    SELECT gc2.id
    FROM olympics.games_competitor gc2
    JOIN olympics.competitor_event ce2 ON gc2.id = ce2.competitor_id
    GROUP BY gc2.person_id, gc2.games_id
    HAVING COUNT(ce2.event_id) > 1
)
GROUP BY gc.person_id, gc.games_id;

-- Task 3: Identify regions where the average number of medals won per 
-- competitor is greater than the overall average. Use subqueries to calculate and compare averages.

SELECT nr.region_name
FROM olympics.noc_region nr
JOIN olympics.person_region pr ON nr.id = pr.region_id
JOIN olympics.games_competitor gc ON pr.person_id = gc.person_id
JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
GROUP BY nr.region_name
HAVING AVG(
    (SELECT COUNT(ce2.medal_id)
     FROM olympics.competitor_event ce2
     WHERE ce2.competitor_id = gc.id)
) > (
    SELECT AVG(total_medals)
    FROM (
        SELECT gc2.id AS competitor_id, COUNT(ce2.medal_id) AS total_medals
        FROM olympics.games_competitor gc2
        JOIN olympics.competitor_event ce2 ON gc2.id = ce2.competitor_id
        GROUP BY gc2.id
    ) AS competitor_medals
);

-- Task 4: Create a temporary table to track competitors’ participation across 
-- different seasons and identify those who have participated in both Summer and Winter games.


CREATE TEMPORARY TABLE temp_competitor_seasons AS
SELECT gc.person_id AS competitor_id, g.season
FROM olympics.games_competitor gc
JOIN olympics.games g ON gc.games_id = g.id;

SELECT competitor_id
FROM temp_competitor_seasons
GROUP BY competitor_id
HAVING COUNT(DISTINCT season) = 2;

DROP TABLE temp_competitor_seasons;