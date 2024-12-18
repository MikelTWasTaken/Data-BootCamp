    CREATE TABLE IF NOT EXISTS Transaction (
        transaction_id SERIAL PRIMARY KEY,
        customer_id INT,
        transaction_date TIMESTAMP NOT NULL,
        transaction_amount DECIMAL(10, 2) NOT NULL,
        rounded_amount DECIMAL(10, 2) NOT NULL,
        unrounded_difference DECIMAL(10, 2) NOT NULL,
        category VARCHAR(50),
        merchant_name VARCHAR(100),
        FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
    );