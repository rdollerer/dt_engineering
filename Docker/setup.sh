#!/bin/sh

# Build Docker images
docker-compose build

# Run Docker Compose
docker-compose up --abort-on-container-exit

# Clean up
docker-compose down
