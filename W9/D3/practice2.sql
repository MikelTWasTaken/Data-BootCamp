-- Create Patients Table (1st Normal Form)
CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE
);
-- Create Visits Table (2nd Normal Form, normalized from the patient data)
CREATE TABLE visits (
    visit_id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(patient_id),
    visit_date DATE,
    diagnosis VARCHAR(100)
);
-- Insert data into patients table
INSERT INTO patients (first_name, last_name, date_of_birth)
VALUES
    ('John', 'Doe', '1985-02-20'),
    ('Jane', 'Smith', '1990-05-15'),
    ('Emily', 'Johnson', '1982-08-25');
-- Insert data into visits table
INSERT INTO visits (patient_id, visit_date, diagnosis)
VALUES
    (1, '2024-01-10', 'Flu'),
    (1, '2024-02-20', 'Cold'),
    (2, '2024-03-05', 'Headache'),
    (3, '2024-04-10', 'Diabetes');