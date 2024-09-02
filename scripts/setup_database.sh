#!/bin/bash

DB_NAME="cafe_ordering_system"
DB_USER="postgres"     # Replace with your database user
DB_PASSWORD="postgres" # Replace with your database password
SQL_FILE="cafe_ordering_system.sql" # Name of the SQL file containing the schema and data

# Check if the database exists
DB_EXISTS=$(psql -U "$DB_USER" -lqt | cut -d \| -f 1 | grep -w "$DB_NAME")

if [ "$DB_EXISTS" ]; then
    echo "Database '$DB_NAME' already exists. Forcing disconnection of active connections..."
    psql -U "$DB_USER" -c "SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = '$DB_NAME' AND pid <> pg_backend_pid();" 

    echo "Dropping the database..."
    dropdb -U "$DB_USER" "$DB_NAME"
    echo "Database '$DB_NAME' dropped."
fi

# Create the database
echo "Creating database '$DB_NAME'..."
createdb -U "$DB_USER" "$DB_NAME"

# Execute the SQL script
echo "Loading schema and data into '$DB_NAME'..."
psql -U "$DB_USER" -d "$DB_NAME" -f "$SQL_FILE"

echo "Database setup complete."
