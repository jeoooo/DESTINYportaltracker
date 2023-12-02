import os
import time
import requests
import certifi
from urllib3.exceptions import InsecureRequestWarning
import logging
from dotenv import load_dotenv
from classes.website_checker import check_website_uptime, insert_website_status

# Load environment variables from the .env file
load_dotenv()

# Set up logging configuration
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO  # Set the desired logging level
)

# Your API key loaded from the .env file
# TESTING_URL
base_url = os.getenv("TESTING_URL", "TESTING_URL")
api_path = "/api/collections/website/records?skipTotal=false"
api_url = base_url + api_path

try:
    while True:
        response = requests.get(api_url, verify=certifi.where())

        if response.status_code == 200:
            data = response.json()

            items = data.get("items", [])

            for item in items:
                school_id = item.get("school_id")
                website_id = item.get("id")
                original_url = item.get("url")

                uptime_status_code = check_website_uptime(original_url)

                try:
                    uptime_status_code = int(uptime_status_code)
                except ValueError:
                    logging.error(f"Invalid status code for {original_url}: {uptime_status_code}")
                    continue

                if 200 <= uptime_status_code < 300:
                    description = "OK"
                elif 400 <= uptime_status_code < 500:
                    description = "Client Error"
                elif 500 <= uptime_status_code < 600:
                    description = "Server Error"
                else:
                    description = f"{uptime_status_code}"

                insert_website_status(school_id, website_id, uptime_status_code, description)

                logging.info(f"School ID: {school_id}")
                logging.info(f"Website ID: {website_id}")
                logging.info(f"URL: {original_url}")
                logging.info(f"{description}")
                logging.info(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n")

        else:
            logging.error(f"Error: {response.status_code}")
            logging.error(response.text)

        for remaining_time in range(30, 0, -1):
            logging.info(f"Checking in the next {remaining_time} seconds...")
            time.sleep(1)

except Exception as e:
    logging.error(f"An unexpected error occurred: {e}")
