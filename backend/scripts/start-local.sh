#!/usr/bin/env sh
#
# A script to start the API server in a local mode (not containerized)
# This is meant to be a way to isolate the API server for debugging/testing.
#

export $(grep -v '^#' .env | xargs)

# Create all tables if the database is empty.
python -m app.db

# Run database schema migrations (if any).
alembic upgrade head

python -m uvicorn app.main:app --host 0.0.0.0 --port 3000
