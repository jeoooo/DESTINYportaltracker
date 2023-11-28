# src/classes/website_checker.py
import time
import requests
import logging  # Import the logging module
from .api_handler import check_website_uptime

# Set up logging configuration
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO  # Set the desired logging level
)

def insert_website_status(school_id, website_id, status_code, description):
    url = "http://127.0.0.1:8090/api/collections/website_status/records"
    timestamp = int(time.time())
    api_key = '55d219232510d0da2575621e5ac5b61c'  # Hardcoded API key

    payload = {
        'school_id': school_id,
        'website_id': website_id,
        'status_code': status_code,
        'description': description,
        'timestamp': timestamp,
        'api_key': api_key,
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, json=payload, headers=headers)

    logging.info(response.text)