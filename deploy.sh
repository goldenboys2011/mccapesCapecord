#!/bin/bash

set -e

echo "======================================"
echo " Updating MCCapes CapeCord Bot"
echo "======================================"

# Go to your project directory
cd /mccapesCapecord/

echo ""
echo "Stopping running containers..."
sudo docker compose down

echo ""
echo "Pulling latest changes..."
git pull

echo ""
echo "Building Docker image..."
sudo docker build -t mccapescapecord-bot .

echo ""
echo "Available Docker images:"
sudo docker images

echo ""
echo "Starting containers..."
sudo docker compose up -d

echo ""
echo "======================================"
echo " Deployment complete!"
echo "======================================"