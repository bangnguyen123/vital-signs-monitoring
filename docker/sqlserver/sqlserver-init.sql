CREATE DATABASE vitals;
GO
USE vitals;
GO
CREATE TABLE vital_signs (
  patient_id INT,
  timestamp VARCHAR(50),
  heart_rate INT
);
GO