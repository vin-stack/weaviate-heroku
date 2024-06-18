#!/bin/sh

# Start Weaviate
weaviate &

# Wait for Weaviate to start
sleep 10

# Start the Flask app
python app.py
