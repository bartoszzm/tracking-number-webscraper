#USPS delivery status tracker
#uses google sheets and updates multiple deliver at a time

import time
import logging
from bs4 import BeautifulSoup
import requests
import gspread

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Specify the location of the service account JSON file
SERVICE_ACCOUNT_FILE_PATH = r'C:\Users\musio\Desktop\python project\webscraping tracking status\service_account.json'

# Connect to the Google Sheet
service_account = gspread.service_account(filename=SERVICE_ACCOUNT_FILE_PATH)
work_book = service_account.open("TrackingStatus")
work_book_sheet = work_book.worksheet("MainSheet")

# Set the user-agent header to identify as a browser
HEADERS = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

def get_tracking_url(cell_value):
    return f"https://tools.usps.com/go/TrackConfirmAction.action?tLabels={cell_value}"

def extract_clean_text(element):
    return element.string.replace("\n", "").replace("\t", "").strip() if element else ""

# Get the total number of rows in the worksheet
total_rows = work_book_sheet.row_count

# Use list comprehension to get a list of tracking numbers
tracking_numbers = [work_book_sheet.cell(row_number, 1).value for row_number in range(2, total_rows + 1)]

# Iterate over the tracking numbers
for cell_value in tracking_numbers:
    try:
        # Check if the cell is empty
        if not cell_value:
            logging.info("Empty cell encountered. Stopping the loop.")
            break

        # Construct the USPS tracking URL with the tracking number
        url = get_tracking_url(cell_value)

        # Send a GET request to the USPS website
        result = requests.get(url, headers=HEADERS)
        doc = BeautifulSoup(result.content, "html.parser")

        # Extract the delivery status and date from the USPS website
        status = doc.find(class_="tb-status-detail")
        date = doc.find(class_="tb-date")
        date_cute = extract_clean_text(date)

        # Update the Google Sheet with the delivery status and date
        work_book_sheet.update_cell(row_number, 2, extract_clean_text(status))
        work_book_sheet.update_cell(row_number, 3, date_cute)

        # Print the tracking URL and delivery status for verification
        logging.info(f"Tracking URL: {url}")
        logging.info(f"Delivery Status: {status}")

        # Wait for 2 seconds before processing the next row
        time.sleep(2)

        # For additional checking:
        #   - Print the delivery date
        #   - Print the tracking number from the cell
        #   - Uncomment the lines below:
        # logging.info(f"Delivery Date: {date_cute}")
        # logging.info(f"Tracking Number: {cell_value}")

    except Exception as e:
        # Log any exceptions that occur during the execution
        logging.error(f"An error occurred for tracking number {cell_value}: {e}")
