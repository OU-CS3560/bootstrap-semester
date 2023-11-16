#!/bin/sh
#
# A script to start the API server from within a container.
#

# Wait for DB to be ready.
python -m app.wait_db

if [ $? -eq 1 ] 
then
    echo "wait_db.py exited with code 1. Database is not ready"
else
    # Create all tables if the database is empty.
    python -m app.db

    # Run database schema migrations (if any).
    alembic upgrade head

    # Start the API server.
    uvicorn app.main:app --host 0.0.0.0 --port 80 --proxy-headers --root-path /api
fi
