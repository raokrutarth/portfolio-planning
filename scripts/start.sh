#!/bin/bash -ex

# Start a local instance of the application

# set pythonpath
export PYTHONPATH=${PYTHONPATH}:"$(pwd)/app"

# poetry run gunicorn \
#     --bind=0.0.0.0:5000 \
#     --workers 2 \
#     --worker-class uvicorn.workers.UvicornWorker \
#     --log-level info \
#     --reload \
#     main:app

poetry run uvicorn main:app --host 0.0.0.0 --port 5000 --workers 4 --reload