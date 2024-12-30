-- Task: Find the employee details who have the highest salary in each department.

SELECT d.department_name, e.first_name, e.last_name, e.salary
FROM (
    SELECT department_id, MAX(salary) AS max_salary
    FROM employees
    GROUP BY department_id
) 
JOIN employees e ON e.department_id = m.department_id AND e.salary = m.max_salary
JOIN departments d ON e.department_id = d.department_id;

-- Task: List the employees who work in departments located in either New York or London.

SELECT first_name, last_name
FROM employees e
WHERE EXISTS (
    SELECT 1
    FROM departments d
    JOIN locations l ON d.location_id = l.location_id
    WHERE e.department_id = d.department_id
    AND l.city IN ('London', 'New York')
);

-- Task: Find employees whose salary is above the departmental average, but only for departments located in the USA.
SELECT e.employee_id, e.first_name, e.last_name, e.salary
FROM employees e
WHERE e.department_id IN (
    SELECT d.department_id
    FROM departments d
    JOIN locations l ON d.location_id = l.location_id
    WHERE l.country = 'USA'
)
AND e.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e.department_id
);