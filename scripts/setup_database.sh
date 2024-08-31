#!/bin/bash

DB_NAME="cafe_ordering_system"
DB_USER="postgres"     # Replace with your database user
DB_PASSWORD="postgres" # Replace with your database password
SQL_FILE="cafe_ordering_system.sql" # Name of the SQL file containing the schema and data

# Check if the database exists
DB_EXISTS=$(psql -U "$DB_USER" -lqt | cut -d \| -f 1 | grep -w "$DB_NAME")

if [ "$DB_EXISTS" ]; then
    echo "Database '$DB_NAME' already exists. Skipping creation."
else
    # Create the database
    echo "Creating database '$DB_NAME'..."
    # -- Create the main database
    # --CREATE DATABASE cafe_ordering_system;
    createdb -U "$DB_USER" "$DB_NAME"
fi

# Execute the SQL script
echo "Loading schema and data into '$DB_NAME'..."
psql -U "$DB_USER" -d "$DB_NAME" -f "$SQL_FILE"

echo "Database setup complete."
