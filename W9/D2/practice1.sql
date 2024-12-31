
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT,
    salary DECIMAL(10, 2)
);

CREATE TABLE sales_data (
    sale_id INT PRIMARY KEY,
    employee_id INT,
    sales DECIMAL(10, 2),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

INSERT INTO employees (employee_id, first_name, last_name, department_id, salary) VALUES
(1, 'John', 'Doe', 1, 60000),
(2, 'Jane', 'Smith', 2, 80000),
(3, 'Jim', 'Brown', 3, 90000),
(4, 'Jake', 'White', 4, 70000),
(5, 'Jill', 'Green', 5, 75000),
(6, 'Jack', 'Black', 3, 95000),
(7, 'Jerry', 'Gray', 2, 82000);

INSERT INTO sales_data (sale_id, employee_id, sales) VALUES
(1, 1, 1000),
(2, 2, 1500),
(3, 3, 2000),
(4, 4, 700),
(5, 5, 1300),
(6, 6, 1750),
(7, 7, 1200);

--The ROW_NUMBER() function assigns a unique number to each row within a partition of a result set,
--starting at 1 for the first row in each partition. Think of it as giving a unique serial number to each row.
--The RANK() function assigns a rank to each row within a partition of a result set.
--If two rows have the same value, they receive the same rank, and the next rank(s) are skipped.
--The DENSE_RANK() function is similar to RANK(), but it does not skip any ranks after ties.
-- select *  FROM employees;
-- SELECT department_id, employee_id, salary,
--        ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS row_number,
-- 	   RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank,
--        DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dense_rank
-- FROM employees;