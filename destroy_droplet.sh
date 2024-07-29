#!/bin/bash

# You MUST destroy all droplets.

# Set your DigitalOcean API token here
API_TOKEN="cc3032-pat-14: dop_v1_3ebf9b2810626808748d47f539457288cc1cb2472143e676cd828b0b5faaef9c"

# Read the droplet ID from the file
DROPLET_ID=$(cat droplet_id.txt)

# Destroy the droplet using the DigitalOcean API
curl -k -X DELETE "https://api.digitalocean.com/v2/droplets/$DROPLET_ID" \
    -H "Authorization: Bearer $API_TOKEN"

echo "Droplet with ID $DROPLET_ID has been destroyed"
