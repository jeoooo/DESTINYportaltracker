# src/classes/api_handler.py
import os
import requests
import logging  # Import the logging module
import certifi
import warnings
from dotenv import load_dotenv
from urllib3.exceptions import InsecureRequestWarning
# Load environment variables from the .env file
# from dotenv import load_dotenv
# load_dotenv()

# Set up logging configuration
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO  # Set the desired logging level
)

# Specify the custom path for the CA certificate bundle
custom_ca_path = os.getenv("CA_CERTIFICATE_PATH")

# Suppress only the InsecureRequestWarning caused by unverified HTTPS requests
# warnings.filterwarnings("ignore", category=InsecureRequestWarning)

def check_website_uptime(url):
    try:
        response = requests.get(url, verify=custom_ca_path)

        return response.status_code
    except requests.ConnectionError as e:
        error_msg = str(e)
        return f"Failed to connect to the website {url}. Exception: {error_msg}"
