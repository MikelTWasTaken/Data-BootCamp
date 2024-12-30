-- INSERT INTO high_salary_employees (employee_id, first_name, last_name, salary)
-- SELECT employee_id, first_name, last_name, salary
-- FROM employees
-- WHERE salary > (SELECT AVG(salary) FROM employees);

-- UPDATE employees
-- SET salary = salary * 1.1
-- WHERE department_id = (SELECT department_id
--                        FROM departments
--                        WHERE department_name = 'IT');

-- Task: Insert new employees into a promotion list if their salary is above the department average.

INSERT INTO promotion_list (employee_id, first_name, last_name, salary)
SELECT e.employee_id, e.first_name, e.last_name, e.salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department_id = d.department_id
);

-- Task: Increase the salary of employees in departments with below-average total sales.

UPDATE employees
SET salary = salary * 1.1
WHERE department_id IN (
    SELECT department_id
    FROM (
        SELECT d.department_id, SUM(s.sales) AS department_total_sales
        FROM departments d
        JOIN sales s ON d.department_id = s.department_id
        GROUP BY d.department_id
    ) department_sales
    WHERE department_total_sales < (
        SELECT AVG(department_total_sales)
        FROM (
            SELECT SUM(s.sales) AS department_total_sales
            FROM sales s
            JOIN departments d ON s.department_id = d.department_id
            GROUP BY d.department_id
        ) avg_department_sales
    )
);

