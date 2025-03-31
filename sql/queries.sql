-- CTE for abnormal readings
WITH abnormal_readings AS (
    SELECT patient_id, timestamp, heart_rate
    FROM vital_signs
    WHERE heart_rate > 100
)
SELECT patient_id, COUNT(*) AS abnormal_count
FROM abnormal_readings
GROUP BY patient_id;

-- Window function for ranking
SELECT patient_id, timestamp, heart_rate,
       RANK() OVER (PARTITION BY patient_id ORDER BY heart_rate DESC) AS hr_rank
FROM vital_signs;