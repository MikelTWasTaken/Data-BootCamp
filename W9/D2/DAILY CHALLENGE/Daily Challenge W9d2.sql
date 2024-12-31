-- Task 1: Calculate the Average Budget Growth Rate for Each Production Company
-- Calculate the average budget growth rate for each production company across all movies they have produced.
-- Use window functions to determine the budget growth rate and then calculate the average growth rate.

WITH BudgetGrowth AS (
    SELECT
        pc.company_name,
        m.budget,
        LAG(m.budget) OVER (PARTITION BY pc.company_name ORDER BY m.release_date) AS prev_budget
    FROM
        movies.movie m
    JOIN
        movies.movie_company mc ON m.movie_id = mc.movie_id
    JOIN
        movies.production_company pc ON mc.company_id = pc.company_id
),
AverageGrowth AS (
    SELECT
        company_name,
        AVG((budget - prev_budget) * 1.0 / NULLIF(prev_budget, 0)) AS avg_growth_rate
    FROM
        BudgetGrowth
    WHERE
        prev_budget IS NOT NULL
          AND prev_budget != 0
    GROUP BY
        company_name
)
SELECT
    company_name,
    avg_growth_rate
FROM
    AverageGrowth
ORDER BY
    avg_growth_rate DESC;

-- 🌟 Task 2: Determine the Most Consistently High-Rated Actor
-- Identify the actor who has appeared in the most movies that are rated above the average 
-- rating of all movies. Use window functions and CTEs to calculate the average rating and filter 
-- the actors based on this criterion.

-- Calculate the most consistently high-rated actor
WITH AverageRating AS (
    SELECT
        AVG(m.vote_average) AS overall_avg_rating
    FROM
        movies.movie m
),
HighRatedMovies AS (
    SELECT
        mc.person_id,
        COUNT(*) AS high_rated_count
    FROM
        movies.movie_cast mc
    JOIN
        movies.movie m ON mc.movie_id = m.movie_id
    CROSS JOIN
        AverageRating ar
    WHERE
        m.vote_average > ar.overall_avg_rating
    GROUP BY
        mc.person_id
),
ActorDetails AS (
    SELECT
        hrm.person_id,
        hrm.high_rated_count,
        p.person_name
    FROM
        HighRatedMovies hrm
    JOIN
        movies.person p ON hrm.person_id = p.person_id
)
SELECT
    person_name,
    high_rated_count
FROM
    ActorDetails
ORDER BY
    high_rated_count DESC
LIMIT 1;


-- 🌟 Task 3: Calculate the Rolling Average Revenue for Each Genre
-- Calculate the rolling average revenue for movies within each genre, considering only the 
-- last three movies released in the genre. Use window functions with the ROWS frame specification to achieve this.

SELECT
    g.genre_name,
    m.title AS movie_title,
    m.release_date,
    m.revenue,
    AVG(m.revenue) OVER (
        PARTITION BY g.genre_name
        ORDER BY m.release_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS rolling_avg_revenue
FROM
    movies.movie_genres mg
JOIN
    movies.genre g ON mg.genre_id = g.genre_id
JOIN
    movies.movie m ON mg.movie_id = m.movie_id
WHERE
    m.revenue IS NOT NULL
ORDER BY
    g.genre_name,
    m.release_date;


-- 🌟 Task 4: Identify the Highest-Grossing Movie Series
-- Identify the movie series (based on shared keywords) with the highest total revenue. 
-- Use window functions and CTEs to group movies by their series and calculate the total revenue.

WITH KeywordRevenue AS (
    SELECT
        k.keyword_name AS series_name,
        m.title AS movie_title,
        m.revenue
    FROM
        movies.movie_keywords mk
    JOIN
        movies.keyword k ON mk.keyword_id = k.keyword_id
    JOIN
        movies.movie m ON mk.movie_id = m.movie_id
    WHERE
        m.revenue IS NOT NULL
),
SeriesTotalRevenue AS (
    SELECT
        series_name,
        SUM(revenue) AS total_revenue
    FROM
        KeywordRevenue
    GROUP BY
        series_name
)
SELECT
    series_name AS movie_series,
    total_revenue
FROM
    SeriesTotalRevenue
ORDER BY
    total_revenue DESC
LIMIT 1;
