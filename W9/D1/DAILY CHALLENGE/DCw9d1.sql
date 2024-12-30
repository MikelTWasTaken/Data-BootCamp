-- 🌟 Exercise 1: Detailed Medal Analysis


-- SQL Dataset we will be using
-- Olympic Data
-- Task 1: Identify competitors who have won at least one medal in events spanning both Summer 
-- and Winter Olympics. Create a temporary table to store these competitors and their medal counts 
-- for each season, and then display the contents of this table.

CREATE TEMPORARY TABLE temp_medal_counts AS
SELECT
    gc.person_id AS competitor_id,
    g.season AS season,
    COUNT(ce.medal_id) AS medal_count
FROM olympics.games_competitor gc
JOIN olympics.games g ON gc.games_id = g.id
JOIN olympics.competitor_event ce ON ce.competitor_id = gc.id
WHERE ce.medal_id IS NOT NULL -- Only include rows where a medal was won
GROUP BY gc.person_id, g.season;

CREATE TEMPORARY TABLE temp_both_seasons AS
SELECT
    tmc.competitor_id,
    SUM(CASE WHEN tmc.season = 'Summer' THEN tmc.medal_count ELSE 0 END) AS summer_medals,
    SUM(CASE WHEN tmc.season = 'Winter' THEN tmc.medal_count ELSE 0 END) AS winter_medals
FROM temp_medal_counts tmc
GROUP BY tmc.competitor_id
HAVING COUNT(DISTINCT tmc.season) = 2;

SELECT * FROM temp_both_seasons;


-- Task 2: Create a temporary table to store competitors who have won medals in exactly 
-- two different sports, and then use a subquery to identify the top 3 competitors with 
-- the highest total number of medals across all sports. Display the contents of this table.
CREATE TEMPORARY TABLE temp_two_sport_medalists AS
SELECT
    ce.competitor_id,
    COUNT(DISTINCT sp.id) AS sports_count,
    COUNT(ce.medal_id) AS total_medals
FROM olympics.competitor_event ce
JOIN olympics.event e ON ce.event_id = e.id
JOIN olympics.sport sp ON e.sport_id = sp.id
WHERE ce.medal_id IS NOT NULL
GROUP BY ce.competitor_id
HAVING COUNT(DISTINCT sp.id) = 2;

CREATE TEMPORARY TABLE temp_top_medalists AS
SELECT
    tsm.competitor_id,
    tsm.total_medals
FROM temp_two_sport_medalists tsm
ORDER BY tsm.total_medals DESC
LIMIT 3;

SELECT * FROM temp_top_medalists;

-- 🌟 Exercise 2: Region and Competitor Performance
-- Task 1: Retrieve the regions that have competitors who have won the highest number 
-- of medals in a single Olympic event. Use a subquery to determine the event with 
-- the highest number of medals for each competitor, and then display the top 5 regions 
-- with the highest total medals.

CREATE TEMPORARY TABLE temp_competitor_event_medals AS
SELECT
    ce.competitor_id,
    ce.event_id,
    COUNT(ce.medal_id) AS medal_count
FROM olympics.competitor_event ce
WHERE ce.medal_id IS NOT NULL
GROUP BY ce.competitor_id, ce.event_id;

CREATE TEMPORARY TABLE temp_region_medals AS
SELECT
    pr.region_id,
    SUM(tcem.medal_count) AS total_medals
FROM temp_competitor_event_medals tcem
JOIN olympics.games_competitor gc ON tcem.competitor_id = gc.id
JOIN olympics.person_region pr ON gc.person_id = pr.person_id
GROUP BY pr.region_id;

SELECT
    nr.region_name,
    trm.total_medals
FROM temp_region_medals trm
JOIN olympics.noc_region nr ON trm.region_id = nr.id
ORDER BY trm.total_medals DESC
LIMIT 5;

-- Task 2: Create a temporary table to store competitors who have participated in more than three 
-- Olympic Games but have not won any medals. Retrieve and display the contents of this table, 
-- including their full names and the number of games they participated in.

CREATE TEMPORARY TABLE temp_competitor_games_count AS
SELECT
    gc.person_id,
    COUNT(DISTINCT gc.games_id) AS games_count
FROM olympics.games_competitor gc
GROUP BY gc.person_id;

CREATE TEMPORARY TABLE temp_no_medals_competitors AS
SELECT
    tcgc.person_id,
    tcgc.games_count
FROM temp_competitor_games_count tcgc
WHERE tcgc.games_count > 3
AND NOT EXISTS (
    SELECT 1
    FROM olympics.competitor_event ce
    WHERE ce.competitor_id = tcgc.person_id
    AND ce.medal_id IS NOT NULL
);
SELECT
    p.full_name,
    tnm.games_count
FROM temp_no_medals_competitors tnm
JOIN olympics.person p ON tnm.person_id = p.id;