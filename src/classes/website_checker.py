# src/classes/website_checker.py
import os
import time
import requests
import logging
from dotenv import load_dotenv  # Import the load_dotenv function
from classes.api_handler import check_website_uptime

# Load environment variables from the .env file
load_dotenv()

# Set up logging configuration
logging.basicConfig(
    format='\033[97m%(asctime)s - [POCKETBASE - INSERT] - %(levelname)s - %(message)s\033[0m',
    level=logging.INFO  # Set the desired logging level
)

def insert_website_status(school_id, website_id, status_code, description):
    try:
        base_url = os.getenv("PRODUCTION_URL", "http://127.0.0.1:8090")   # run in production, else run locally in your machine
        api_key = os.getenv("API_KEY") # Default API key
        path = "/api/collections/website_status/records" 
        url = base_url + path
        timestamp = int(time.time())

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

        response.raise_for_status()  # Raise HTTPError for bad responses

        logging.info(f"\033[97m{response.text} - School ID: {school_id}, Website ID: {website_id}, Status Code: {status_code}, Description: {description}, Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\033[0m")

    except requests.exceptions.RequestException as e:
        logging.error(f"\033[97mRequest failed: {e}\033[0m")
