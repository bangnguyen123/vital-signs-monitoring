CREATE TABLE vital_signs (
    id SERIAL PRIMARY KEY,
    patient_id INT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    heart_rate INT,
    blood_pressure VARCHAR(7),
    temperature DECIMAL(3,1)
);
