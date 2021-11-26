#!/usr/bin/env bash

set -u
set -e

# Wait for database
echo "Waiting for postgresql..."
sleep 10


# Initialize server data
./manage.py migrate --noinput
./manage.py loaddata /build/fixtures/fixtures.json


./manage.py runserver "0.0.0.0:8000"

