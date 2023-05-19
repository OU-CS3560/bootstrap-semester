#!/bin/sh

# Wait for DB to be ready.
python /code/app/wait_db.py

# Database migrations
alembic upgrade head

# Start the API server.
uvicorn app.main:app --host 0.0.0.0 --port 80 --proxy-headers --root-path /api
