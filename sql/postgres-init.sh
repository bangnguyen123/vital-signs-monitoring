#!/bin/bash

# Wait for PostgreSQL to be ready
until pg_isready -h postgres -U postgres; do
    echo "Waiting for PostgreSQL..."
    sleep 2
done

# Execute the SQL script
psql -U postgres -d vitals -f /sql/create_tables.sql