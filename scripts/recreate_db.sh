#!/bin/bash
# Script to recreate the restaurant database and apply migrations

set -e  # Exit on error

echo "Creating database user (if not exists)..."
psql -U postgres -c "CREATE USER restaurant_user WITH PASSWORD 'restaurant_dev_pass';" 2>/dev/null || echo "User already exists"

echo "Dropping existing database (if exists)..."
psql -U postgres -c "DROP DATABASE IF EXISTS restaurant_db;"

echo "Creating database..."
psql -U postgres -c "CREATE DATABASE restaurant_db OWNER restaurant_user;"

echo "Applying migrations..."
uv run alembic upgrade head

echo "Database recreated successfully!"
