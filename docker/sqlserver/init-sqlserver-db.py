import pyodbc
import time

# Connection details
server = 'sqlserver'  # Matches Docker service name
database = 'master'   # Initial connection to master
username = 'sa'
password = 'StrongPass!'  # Match your docker-compose.yml

# Connection string
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password}"
)

print(conn_str)
# SQL commands
init_sql = """
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'vitals')
    CREATE DATABASE vitals;
GO

USE vitals;
GO

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'vital_signs')
    CREATE TABLE vital_signs (
        patient_id INT,
        timestamp VARCHAR(50),
        heart_rate INT,
        temperature FLOAT,
        PRIMARY KEY (patient_id, timestamp)
    );
GO
"""

# Retry logic to wait for SQL Server to start
max_retries = 10
for attempt in range(max_retries):
    try:
        conn = pyodbc.connect(conn_str, timeout=5)
        cursor = conn.cursor()
        print("Connected to SQL Server!")
        break
    except pyodbc.Error as e:
        print(f"Attempt {attempt + 1}/{max_retries} failed: {e}")
        if attempt == max_retries - 1:
            raise Exception("Failed to connect to SQL Server after retries")
        time.sleep(5)

# Execute initialization
for statement in init_sql.split('GO'):
    if statement.strip():
        cursor.execute(statement)

conn.commit()
print("Database and table initialized!")
conn.close()