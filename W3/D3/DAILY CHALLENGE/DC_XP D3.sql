-- PART 1
-- CREATE TABLE Customers (
--     id SERIAL PRIMARY KEY,
--     first_name VARCHAR(50) NOT NULL,
--     last_name VARCHAR(50) NOT NULL
-- );

-- CREATE TABLE Customer_Profile (
--     id SERIAL PRIMARY KEY,
--     isLoggedIn BOOLEAN DEFAULT false,
--     customer_id INT UNIQUE,
--     CONSTRAINT fk_customers FOREIGN KEY (customer_id) REFERENCES Customers (id) ON DELETE CASCADE
-- );

-- INSERT INTO Customers (first_name, last_name) VALUES ('John', 'Doe');
-- INSERT INTO Customers (first_name, last_name) VALUES ('Jerome', 'Lalu');
-- INSERT INTO Customers (first_name, last_name) VALUES ('Lea', 'Rive');

-- INSERT INTO Customer_Profile (isLoggedIn, customer_id)
-- VALUES (true, (SELECT id FROM Customers WHERE first_name = 'John' AND last_name = 'Doe'));

-- INSERT INTO Customer_Profile (isLoggedIn, customer_id)
-- VALUES (false, (SELECT id FROM Customers WHERE first_name = 'Jerome' AND last_name = 'Lalu'));

-- SELECT c.first_name
-- FROM Customer c
-- JOIN Customer_Profile cp ON c.id = cp.customer_id
-- WHERE cp.isLoggedIn = true;

-- SELECT c.first_name, COALESCE(cp.isLoggedIn, false) AS isLoggedIn
-- FROM Customer c
-- LEFT JOIN Customer_Profile cp ON c.id = cp.customer_id;

-- SELECT COUNT(*) AS not_logged_in_count
-- FROM Customer c
-- LEFT JOIN Customer_Profile cp ON c.id = cp.customer_id
-- WHERE cp.isLoggedIn = false OR cp.isLoggedIn IS NULL;

-- PART 2


