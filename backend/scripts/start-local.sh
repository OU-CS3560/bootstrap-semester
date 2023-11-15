#!/usr/bin/env sh
#
# A script to start the API server in a local mode (not containerized)
# This is meant to be a way to isolate the API server for debugging/testing.
#
export $(cat .env)
python -m uvicorn app.main:app --host 0.0.0.0 --port 3000
