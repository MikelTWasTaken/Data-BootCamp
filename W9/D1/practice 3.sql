SELECT d.department_name, e.first_name, e.last_name, e.salary
FROM (
    SELECT department_id, MAX(salary) AS max_salary
    FROM employees
    GROUP BY department_id
) m
JOIN employees e ON e.department_id = m.department_id AND e.salary = m.max_salary
JOIN departments d ON e.department_id = d.department_id;