-- 🌟 Exercise 1: Movie Rankings and Analysis

-- Task 1: Rank Movies by Popularity within Each Genre

-- Use the RANK() function to rank movies by their popularity within each genre. 
-- Display the genre name, movie title, and their rank based on popularity.

SELECT 
    g.genre_name, 
    m.title AS movie_title, 
    RANK() OVER (PARTITION BY g.genre_name ORDER BY m.popularity DESC) AS rank
FROM 
    movies.movie m
JOIN 
    movies.movie_genres mg ON m.movie_id = mg.movie_id
JOIN 
    movies.genre g ON mg.genre_id = g.genre_id
ORDER BY 
    g.genre_name, rank;

-- Task 2: Identify the Top 3 Movies by Revenue within Each Production Company

-- Use the NTILE() function to divide the movies produced by each production company 
-- into quartiles based on revenue. Display the company name, movie title, revenue, and quartile.
WITH RankedMovies AS (
    SELECT 
        pc.company_name, 
        m.title AS movie_title, 
        m.revenue, 
        RANK() OVER (PARTITION BY pc.company_name ORDER BY m.revenue DESC) AS rank
    FROM 
        movies.movie m
    JOIN 
        movies.movie_company mc ON m.movie_id = mc.movie_id
    JOIN 
        movies.production_company pc ON mc.company_id = pc.company_id
    WHERE 
        m.revenue IS NOT NULL AND m.revenue > 0
)
SELECT 
    company_name, 
    movie_title, 
    revenue, 
    rank
FROM 
    RankedMovies
WHERE 
    rank <= 3
ORDER BY 
    company_name, rank;

-- Task 3: Calculate the Running Total of Movie Budgets for Each Genre

-- Use the SUM() function with the ROWS frame specification to calculate the running 
-- total of movie budgets within each genre. Display the genre name, movie title, budget, and running total budget.

WITH GenreBudgets AS (
    SELECT 
        g.genre_name, 
        m.title AS movie_title, 
        m.budget
    FROM 
        movies.movie m
    JOIN 
        movies.movie_genres mg ON m.movie_id = mg.movie_id
    JOIN 
        movies.genre g ON mg.genre_id = g.genre_id
    WHERE 
        m.budget IS NOT NULL AND m.budget > 0
)
SELECT 
    genre_name, 
    movie_title, 
    budget, 
    SUM(budget) OVER (
        PARTITION BY genre_name 
        ORDER BY budget DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total_budget
FROM 
    GenreBudgets
ORDER BY 
    genre_name, running_total_budget DESC;

-- Task 4: Identify the Most Recent Movie for Each Genre

-- Use the FIRST_VALUE() function to find the most recent movie within each genre 
-- based on the release date. Display the genre name, movie title, and release date.

WITH RecentMovies AS (
    SELECT 
        g.genre_name,
        m.title AS movie_title,
        m.release_date,
        RANK() OVER (
            PARTITION BY g.genre_name 
            ORDER BY m.release_date DESC
        ) AS rank
    FROM 
        movies.movie m
    JOIN 
        movies.movie_genres mg ON m.movie_id = mg.movie_id
    JOIN 
        movies.genre g ON mg.genre_id = g.genre_id
    WHERE 
        m.release_date IS NOT NULL
)
SELECT 
    genre_name,
    movie_title,
    release_date
FROM 
    RecentMovies
WHERE 
    rank = 1
ORDER BY 
    genre_name;

-- 🌟 Exercise 2: Cast and Crew Performance Analysis


-- Task 1: Rank Actors by Their Appearance in Movies

-- Use the DENSE_RANK() function to rank actors based on the number of movies they have 
-- appeared in. Display the actor’s name and their rank.

SELECT
    p.person_name AS actor_name,
    DENSE_RANK() OVER (ORDER BY COUNT(m.movie_id) DESC) AS rank
FROM
    movies.person p
JOIN
    movies.movie_cast mc ON p.person_id = mc.person_id
JOIN
    movies.movie m ON mc.movie_id = m.movie_id
GROUP BY
    p.person_name
ORDER BY
    rank;

-- Task 2: Identify the Top Director by Average Movie Rating

-- Use a CTE and the RANK() function to find the director with the highest average 
-- movie rating. Display the director’s name and their average rating.

SELECT
    p.person_name AS actor_name,
    DENSE_RANK() OVER (ORDER BY COUNT(m.movie_id) DESC) AS rank
FROM
    movies.person p
JOIN
    movies.movie_cast mc ON p.person_id = mc.person_id
JOIN
    movies.movie m ON mc.movie_id = m.movie_id
GROUP BY
    p.person_name
ORDER BY
    rank;
-- Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor

-- Use the SUM() function to calculate the cumulative revenue of movies acted by each actor. 
-- Display the actor’s name and the cumulative revenue.


SELECT
    p.person_name AS actor_name,
    SUM(m.revenue) OVER (PARTITION BY p.person_name ORDER BY m.release_date) AS cumulative_revenue
FROM
    movies.person p
JOIN
    movies.movie_cast mc ON p.person_id = mc.person_id
JOIN
    movies.movie m ON mc.movie_id = m.movie_id
ORDER BY
    p.person_name, m.release_date;
	
-- Task 4: Identify the Director Whose Movies Have the Highest Total Budget

-- Use a CTE and a window function to find the director whose movies have the highest total budget. 
-- Display the director’s name and the total budget.

WITH DirectorBudget AS (
    SELECT
        p.person_name AS director_name,
        SUM(m.budget) AS total_budget
    FROM
        movies.person p
    JOIN
        movies.movie_crew mc ON p.person_id = mc.person_id
    JOIN
        movies.movie m ON mc.movie_id = m.movie_id
    WHERE
        mc.job = 'Director'
    GROUP BY
        p.person_name
)
SELECT
    director_name,
    total_budget
FROM
    DirectorBudget
WHERE
    total_budget = (SELECT MAX(total_budget) FROM DirectorBudget);

-- XP GOLD

-- Exercise 1: Comprehensive Movie Revenue and Rating Analysis
-- Task 1: Use the LEAD() and LAG() functions to identify movies where the budget 
-- increased compared to the previous movie but decreased compared to the next movie, 
-- in order of their release dates. Display the movie title, release date, and budget, 
-- along with the previous and next budgets.

WITH BudgetAnalysis AS (
    SELECT
        m.title AS movie_title,
        m.release_date,
        m.budget,
        LAG(m.budget) OVER (ORDER BY m.release_date) AS previous_budget,
        LEAD(m.budget) OVER (ORDER BY m.release_date) AS next_budget
    FROM
        movies.movie m
)
SELECT
    movie_title,
    release_date,
    budget,
    previous_budget,
    next_budget
FROM
    BudgetAnalysis
WHERE
    budget > previous_budget AND budget < next_budget
ORDER BY
    release_date;

-- Task 2: Create a CTE to calculate the moving average rating of movies over a 
-- 5-year window for each genre. Display the genre, movie title, release year, and the moving average rating.

WITH GenreMovieRatings AS (
    SELECT
        g.genre_name,
        m.title AS movie_title,
        EXTRACT(YEAR FROM m.release_date) AS release_year,
        m.vote_average
    FROM
        movies.movie_genres mg
    JOIN
        movies.genre g ON mg.genre_id = g.genre_id
    JOIN
        movies.movie m ON mg.movie_id = m.movie_id
    WHERE
        m.vote_average IS NOT NULL
        AND m.release_date IS NOT NULL
),
MovingAverageRatings AS (
    SELECT
        genre_name,
        movie_title,
        release_year,
        vote_average,
        AVG(vote_average) OVER (
            PARTITION BY genre_name
            ORDER BY release_year
            RANGE BETWEEN 5 PRECEDING AND CURRENT ROW
        ) AS moving_avg_rating
    FROM
        GenreMovieRatings
)
SELECT
    genre_name,
    movie_title,
    release_year,
    ROUND(moving_avg_rating, 2) AS moving_avg_rating
FROM
    MovingAverageRatings
ORDER BY
    genre_name, release_year;

-- Task 3: Use the ROW_NUMBER(), RANK(), and DENSE_RANK() functions to create a 
-- comprehensive ranking system for movies based on revenue within each genre. 
-- Display the genre, movie title, revenue, and their respective row number, rank, and dense rank.
WITH GenreMovieRevenue AS (
    SELECT
        g.genre_name,
        m.title AS movie_title,
        m.revenue
    FROM
        movies.movie_genres mg
    JOIN
        movies.genre g ON mg.genre_id = g.genre_id
    JOIN
        movies.movie m ON mg.movie_id = m.movie_id
    WHERE
        m.revenue IS NOT NULL
),
Rankings AS (
    SELECT
        genre_name,
        movie_title,
        revenue,
        ROW_NUMBER() OVER (
            PARTITION BY genre_name
            ORDER BY revenue DESC
        ) AS row_number,
        RANK() OVER (
            PARTITION BY genre_name
            ORDER BY revenue DESC
        ) AS rank,
        DENSE_RANK() OVER (
            PARTITION BY genre_name
            ORDER BY revenue DESC
        ) AS dense_rank
    FROM
        GenreMovieRevenue
)
SELECT
    genre_name,
    movie_title,
    revenue,
    row_number,
    rank,
    dense_rank
FROM
    Rankings
ORDER BY
    genre_name, rank;

-- Exercise 2: In-Depth Actor and Genre Analysis
-- Task 1: Use the FIRST_VALUE() and LAST_VALUE() functions to find the first and last movie 
-- each actor appeared in. Display the actor’s name, first movie title, first movie release date, 
-- last movie title, and last movie release date.

WITH ActorMovies AS (
    SELECT
        p.person_name AS actor_name,
        m.title AS movie_title,
        m.release_date,
        ROW_NUMBER() OVER (PARTITION BY p.person_name ORDER BY m.release_date ASC) AS row_num_asc,
        ROW_NUMBER() OVER (PARTITION BY p.person_name ORDER BY m.release_date DESC) AS row_num_desc
    FROM
        movies.movie_cast mc
    JOIN
        movies.person p ON mc.person_id = p.person_id
    JOIN
        movies.movie m ON mc.movie_id = m.movie_id
)
SELECT
    actor_name,
    FIRST_VALUE(movie_title) OVER (PARTITION BY actor_name ORDER BY release_date ASC) AS first_movie_title,
    FIRST_VALUE(release_date) OVER (PARTITION BY actor_name ORDER BY release_date ASC) AS first_movie_release_date,
    LAST_VALUE(movie_title) OVER (PARTITION BY actor_name ORDER BY release_date ASC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_movie_title,
    LAST_VALUE(release_date) OVER (PARTITION BY actor_name ORDER BY release_date ASC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_movie_release_date
FROM
    ActorMovies
ORDER BY
    actor_name;

-- Task 2: Create a nested subquery to identify genres where the average movie revenue is above 
-- the overall average movie revenue. Within those genres, use a window function to rank movies 
-- by their popularity. Display the genre, movie title, revenue, and rank.

WITH GenreAverageRevenue AS (
    SELECT
        g.genre_name,
        AVG(m.revenue) AS avg_genre_revenue
    FROM
        movies.movie_genres mg
    JOIN
        movies.movie m ON mg.movie_id = m.movie_id
    JOIN
        movies.genre g ON mg.genre_id = g.genre_id
    GROUP BY
        g.genre_name
),
OverallAverageRevenue AS (
    SELECT
        AVG(revenue) AS avg_overall_revenue
    FROM
        movies.movie
)
SELECT
    g.genre_name,
    m.title AS movie_title,
    m.revenue,
    RANK() OVER (PARTITION BY g.genre_name ORDER BY m.popularity DESC) AS popularity_rank
FROM
    movies.movie m
JOIN
    movies.movie_genres mg ON m.movie_id = mg.movie_id
JOIN
    movies.genre g ON mg.genre_id = g.genre_id
JOIN
    GenreAverageRevenue gar ON g.genre_name = gar.genre_name
JOIN
    OverallAverageRevenue oar
WHERE
    gar.avg_genre_revenue > oar.avg_overall_revenue
ORDER BY
    g.genre_name,
    popularity_rank;

-- Task 3: Use a combination of window functions and CTEs to find actors who have appeared in 
-- movies that have collectively grossed in the top 10% of all movie revenues. Display the actor’s 
-- name and the total revenue of the movies they have appeared in.

WITH MovieRevenueRank AS (
    SELECT
        m.movie_id,
        m.title,
        m.revenue,
        PERCENT_RANK() OVER (ORDER BY m.revenue DESC) AS revenue_percent_rank
    FROM
        movies.movie m
),
TopMovies AS (
    SELECT
        movie_id,
        revenue
    FROM
        MovieRevenueRank
    WHERE
        revenue_percent_rank <= 0.1
)
SELECT
    p.person_name AS actor_name,
    SUM(m.revenue) AS total_revenue
FROM
    movies.movie m
JOIN
    movies.movie_cast mc ON m.movie_id = mc.movie_id
JOIN
    movies.person p ON mc.person_id = p.person_id
JOIN
    TopMovies tm ON m.movie_id = tm.movie_id
GROUP BY
    p.person_name
ORDER BY
    total_revenue DESC;
