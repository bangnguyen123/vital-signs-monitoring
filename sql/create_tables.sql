CREATE TABLE vital_signs (
    patient_id INTEGER,
    timestamp TIMESTAMP,
    heart_rate INTEGER,
    bp INTEGER,
    PRIMARY KEY (patient_id, timestamp)
);

CREATE INDEX idx_timestamp ON vital_signs (timestamp);
CREATE INDEX idx_heart_rate ON vital_signs (heart_rate);

COPY vital_signs (patient_id, timestamp, heart_rate)
FROM '/data/mhealth_vital_signs.csv'
DELIMITER ',' CSV HEADER;
