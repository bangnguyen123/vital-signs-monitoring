-- Example Snowflake script to load data and query
COPY INTO mytable
FROM @my_stage/myfile.csv
FILE_FORMAT = (TYPE = 'CSV');

SELECT * FROM mytable;
