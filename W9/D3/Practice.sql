CREATE TABLE patient_data (
    patient_id INT,
    patient_name VARCHAR(100),
    date_of_birth DATE,
    date_of_visit DATE,
    diagnosis_code VARCHAR(10),
    visit_type VARCHAR(20),
    age INT
);
INSERT INTO patient_data (patient_id, patient_name, date_of_birth, date_of_visit, diagnosis_code, visit_type, age)
VALUES
(1, 'John Doe', '1980-05-15', '2024-03-10', 'A01', 'Checkup', 44),
(2, 'JANE Smith', '1990-08-22', '2024-03-11', 'B02', 'Follow-up', 34),
(3, 'Sam Brown', NULL, '2024-03-12', 'C03', 'Emergency', NULL),  -- Missing date_of_birth and age
(4, 'John doe', '1980-05-15', '2024-03-10', 'A01', 'Checkup', 44),  -- Duplicate row
(5, 'Alice White', '1985-07-30', '2024-03-10', 'D04', 'Checkup', 39),  -- Missing date_of_visit
(6, 'Bob Green', '1978-12-01', '2024-03-14', 'E05', 'Follow-up', 46),
(7, 'Charlie Black', '1982-10-10', '2024-03-10', 'F06', 'Checkup', -42),
(8, 'Daniel Blue', '1995-01-20', '2024-03-15', 'G07', 'Follow-up', 29),
(9, 'Eve White', '2000-02-28', '2024-03-16', 'A01', 'Checkup', 24);
--1. Detecting NULL Values
--SELECT * FROM your_table WHERE your_column IS NULL;

SELECT *
FROM patient_data
WHERE date_of_birth IS NULL OR date_of_visit is NULL OR diagnosis_code IS NULL OR visit_type IS NULL OR age is NULL;

--2.Techniques to Handle Missing Data
--SELECT COALESCE(your_column, 'default_value') FROM your_table;
SELECT COALESCE(date_of_birth, '2000-01-01') FROM patient_data;
UPDATE patient_data
SET date_of_birth = '2024-01-01'
WHERE date_of_birth IS NULL;
-- UPDATE your_table
-- SET your_column = (SELECT AVG(your_column) FROM your_table)
-- WHERE your_column IS NULL;
UPDATE patient_data
SET age = (SELECT AVG(AGE) FROM patient_data)
WHERE age IS NULL;
UPDATE patient_data
SET age = (SELECT AVG(AGE) FROM patient_data)
WHERE age IS NULL;
-- Removing Duplicates
-- 1. Identifying Duplicates
-- SELECT your_column, COUNT(*)
-- FROM your_table
-- GROUP BY your_column
-- HAVING COUNT(*) > 1;
INSERT INTO patient_data (patient_id, patient_name, date_of_birth, date_of_visit, diagnosis_code, visit_type, age)
VALUES
(1, 'John Doe', '1980-05-15', '2024-12-10', 'A01', 'Checkup', 44),
(1, 'John Doe', '1980-05-15', '2024-12-12', 'A01', 'Checkup', 44)
;
SELECT  patient_name, date_of_birth, COUNT(*)
FROM patient_data
GROUP BY patient_name, date_of_birth
HAVING COUNT(*) > 1;
SELECT  *
FROM patient_data
WHERE patient_name =  'John Doe' and  date_of_birth = '1980-05-15'
--2. Deleting Duplicates
-- WITH CTE AS (
--     SELECT your_column, ROW_NUMBER() OVER (PARTITION BY your_column ORDER BY your_column) AS rn
--     FROM your_table
-- )
-- DELETE FROM CTE WHERE rn > 1;
WITH CTE AS (
    SELECT patient_id, date_of_visit,
	ROW_NUMBER() OVER (PARTITION BY  patient_name, date_of_birth ORDER BY date_of_visit) AS row_num
    FROM patient_data
)
DELETE FROM patient_data
WHERE patient_id IN (SELECT patient_id FROM CTE WHERE row_num > 1);
-- Correcting Inconsistent Data
-- 1. Standardizing Data Formats
-- Convert date formats
--SELECT CAST(your_date_column AS DATE) FROM your_table;
-- Convert strings to uppercase
-- SELECT UPPER(your_string_column) FROM your_table;
-- SELECT CONVERT(target_data_type, expression, [style])
UPDATE patient_data
SET date_of_visit = date_of_visit::DATE;
select patient_name, INITCAP(patient_name), UPPER(patient_name) as Upper_
from patient_data
UPDATE patient_data
SET patient_name = INITCAP(patient_name);