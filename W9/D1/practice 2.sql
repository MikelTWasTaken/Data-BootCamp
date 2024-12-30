SELECT first_name, last_name
FROM employees e
WHERE EXISTS (
    SELECT 1
    FROM departments d
    JOIN locations l ON d.location_id = l.location_id
    WHERE e.department_id = d.department_id
    AND l.city = 'London'
);