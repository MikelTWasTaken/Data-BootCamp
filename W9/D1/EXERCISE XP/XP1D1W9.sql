-- Task 1: Find the average age of competitors who have won at least one medal, 
-- grouped by the type of medal they won. Use a correlated subquery to achieve this.

-- competitor_event.medal_id - To identify the type of medal won.
-- medal.medal_name - To get the name of the medal (e.g., Gold, Silver, Bronze).
-- games_competitor.age - To calculate the average age of the competitors.
-- competitor_event.competitor_id - To relate competitors with events.
-- games_competitor.id - To match the competitor ID from competitor_event.

SELECT 
    ce.medal_id,
    (SELECT AVG(gc.age)
     FROM olympics.games_competitor gc
     WHERE gc.id IN (
         SELECT ce2.competitor_id
         FROM olympics.competitor_event ce2
         WHERE ce2.medal_id = ce.medal_id
     )) AS avg_age
FROM 
    olympics.competitor_event ce
WHERE 
    ce.medal_id IS NOT NULL
GROUP BY 
    ce.medal_id;


-- Task 2: Identify the top 5 regions with the highest number of unique 
-- competitors who have participated in more than 3 different events. Use nested subqueries to filter and aggregate the data.

SELECT 
    nr.region_name,
    COUNT(DISTINCT pr.person_id) AS unique_competitors
FROM 
    olympics.person_region pr
JOIN olympics.noc_region nr
    ON pr.region_id = nr.id
WHERE pr.person_id IN (
    SELECT gc.person_id
    FROM olympics.games_competitor gc
    WHERE gc.id IN (
        SELECT ce.competitor_id
        FROM olympics.competitor_event ce
        GROUP BY ce.competitor_id
        HAVING COUNT(DISTINCT ce.event_id) > 3
    )
)
GROUP BY nr.region_name
ORDER BY unique_competitors DESC
LIMIT 5;

-- Task 3: Create a temporary table to store the total number of medals won by 
-- each competitor and filter to show only those who have won more than 2 medals. Use subqueries to aggregate the data.

CREATE TEMPORARY TABLE temp_medals AS
SELECT 
    gc.person_id,
    ce.competitor_id,
    COUNT(ce.medal_id) AS total_medals
FROM 
    olympics.competitor_event ce
JOIN olympics.games_competitor gc
    ON ce.competitor_id = gc.id
WHERE 
    ce.medal_id IS NOT NULL
GROUP BY 
    gc.person_id, ce.competitor_id
HAVING 
    COUNT(ce.medal_id) > 2;

-- Task 4: Use a subquery within a DELETE statement to remove records of 
-- competitors who have not won any medals from a temporary table created for analysis.
DELETE FROM temp_medals
WHERE competitor_id NOT IN (
    SELECT DISTINCT ce.competitor_id
    FROM olympics.competitor_event ce
    WHERE ce.medal_id IS NOT NULL
);