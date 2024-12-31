INSERT INTO employees (employee_id, first_name, last_name, department_id, salary) VALUES
(8, 'Sona', 'Liubich', 1, 60000),
(9, 'Jer', 'Gray', 2, 82000);
INSERT INTO sales_data (sale_id, employee_id, sales) VALUES
(8, 8, 1200),
(9, 9, 1750);


-- Demonstration 1: Using LEAD() and LAG()

select * from employees

SELECT 
    employee_id, 
    first_name, 
    last_name, 
    salary,
       LEAD(salary, 1) OVER (ORDER BY salary) AS next_salary,
       LAG(salary, 1) OVER (ORDER BY salary) AS previous_salary
FROM employees;


-- Demonstration 2: Using FIRST_VALUE() and LAST_VALUE()

SELECT 
    employee_id, 
    first_name, 
    last_name, 
    salary,

 FIRST_VALUE(salary) OVER (ORDER BY salary) AS first_salary,
       LAST_VALUE(salary) OVER (ORDER BY salary ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_salary
FROM employees;

-- Demonstration 3: Aggregations with Window Functions


SELECT 
	e.employee_id, 
	e.first_name, 
	e.last_name, 
	s.sales,
       SUM(s.sales) OVER (ORDER BY e.employee_id) AS running_total
FROM employees e
JOIN sales_data s ON e.employee_id = s.employee_id;


-- Demonstration 4: Frame Specifications with ROWS

SELECT 
	employee_id, 
	first_name, 
	last_name, 
	salary,
       SUM(salary) OVER (ORDER BY salary ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS moving_sum
FROM employees;

-- Demonstration 5: Window Functions with CTEs

WITH EmployeeRanks AS (
    SELECT employee_id, first_name, last_name, department_id, salary,
           RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS salary_rank
    FROM employees
)
SELECT * FROM EmployeeRanks
WHERE salary_rank = 1;