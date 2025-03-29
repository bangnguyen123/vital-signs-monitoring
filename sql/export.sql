-- Example export command
COPY (SELECT * FROM vital_signs) TO '/path/to/export.csv' DELIMITER ',' CSV HEADER;
