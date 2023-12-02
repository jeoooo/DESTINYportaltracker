# src/classes/api_handler.py
import os
import requests
import logging
import certifi
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()

# Set up logging configuration
logging.basicConfig(
    format='\033[92m%(asctime)s - [UPTIME CHECK] %(levelname)s - %(message)s\033[0m',
    level=logging.INFO  # Set the desired logging level
)

# Specify the custom path for the CA certificate bundle
custom_ca_path = os.getenv("CA_CERTIFICATE_PATH")



def check_website_uptime(url):
    try:
        response = requests.get(url, verify=custom_ca_path)

        logging.info(f"\033[92mUptime check for {url} - Status Code: {response.status_code}\033[0m")

        return response.status_code
    except requests.ConnectionError as e:
        error_msg = str(e)
        logging.error(f"\033[92mFailed to connect to the website {url}. Exception: {error_msg}\033[0m")
        return f"Failed to connect to the website {url}. Exception: {error_msg}"
