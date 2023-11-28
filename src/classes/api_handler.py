# src/classes/api_handler.py
import requests
import certifi
from urllib3.exceptions import InsecureRequestWarning
import warnings
import logging  # Import the logging module

# Load environment variables from the .env file
# from dotenv import load_dotenv
# load_dotenv()

# Set up logging configuration
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO  # Set the desired logging level
)


# Suppress only the InsecureRequestWarning caused by unverified HTTPS requests
warnings.filterwarnings("ignore", category=InsecureRequestWarning)

def check_website_uptime(url):
    try:
        if "student.umindanao.edu.ph" in url or "hcdc.edu.ph" in url:
            response = requests.get(url, verify=False)
        else:
            response = requests.get(url, verify=certifi.where())

        return response.status_code
    except requests.ConnectionError as e:
        error_msg = str(e)
        return f"Failed to connect to the website {url}. Exception: {error_msg}"

