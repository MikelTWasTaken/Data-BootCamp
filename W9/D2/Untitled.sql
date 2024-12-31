-- Exercise 1: Employee Salaries
-- 1. Task: Use the ROW_NUMBER() function to list employees in each department, 
-- ordered by their salary in descending order. Display the department, 
-- employee name, and their salary rank within the department.

SELECT 
    department_id, 
    employee_id, 
    first_name, 
    last_name, 
    salary,
    ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS row_num
FROM employees;

-- 2. Task: Calculate the cumulative salary for employees in each department using the SUM() function with windowing.

SELECT 
    department_id, 
    employee_id, 
    first_name, 
    last_name, 
    salary,
    SUM(salary) OVER (PARTITION BY department_id ORDER BY salary DESC) AS cumulative_salary
FROM employees;


-- Exercise 2: Sales Performance
-- 1. Task: Rank the sales performance of employees within each department using the DENSE_RANK() function. 
-- Display the department, employee name, and their sales rank.

SELECT 
    e.department_id, 
    e.first_name, 
    e.last_name, 
    sd.sales,
    DENSE_RANK() OVER (PARTITION BY e.department_id ORDER BY sd.sales DESC) AS sales_rank
FROM employees e
JOIN sales_data sd 
    ON e.employee_id = sd.employee_id;

-- 2. Task: Calculate the total sales for each employee and the running total of sales across
-- all employees using the SUM() function with windowing.

SELECT 
    e.employee_id,
    e.first_name, 
    e.last_name, 
    SUM(sd.sales) AS total_sales,
    SUM(SUM(sd.sales)) OVER (ORDER BY e.employee_id) AS running_total_sales
FROM employees e
JOIN sales_data sd 
    ON e.employee_id = sd.employee_id
GROUP BY e.employee_id, e.first_name, e.last_name
ORDER BY e.employee_id;