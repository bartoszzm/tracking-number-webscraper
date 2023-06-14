import time
import logging
from bs4 import BeautifulSoup
import requests
import gspread

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Specify the location of the service account JSON file
service_account_file = r'C:\Users\musio\Desktop\python project\webscraping tracking status\service_account.json'

# Connect to the Google Sheet
service_account = gspread.service_account(filename=service_account_file)
work_book = service_account.open("TrackingStatus")
work_book_sheet = work_book.worksheet("MainSheet")

# Set the user-agent header to identify as a browser
headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

# Get the total number of rows in the worksheet
total_rows = work_book_sheet.row_count

# Iterate over the rows
for row_number in range(2, total_rows + 1):

    try:
        # Get the tracking number from the cell in the Google Sheet
        cell = work_book_sheet.cell(row_number, 1).value

        # Check if the cell is empty
        if not cell:
            logging.info("Empty cell encountered. Stopping the loop.")
            break

        # Construct the USPS tracking URL with the tracking number
        url = f"https://tools.usps.com/go/TrackConfirmAction.action?tLabels={cell}"

        # Send a GET request to the USPS website
        result = requests.get(url, headers=headers)
        doc = BeautifulSoup(result.content, "html.parser")

        # Extract the delivery status and date from the USPS website
        status = doc.find(class_="tb-status-detail")
        date = doc.find(class_="tb-date")
        date_cute = date.string.replace("\n", "").replace("\t", "").strip()

        # Update the Google Sheet with the delivery status and date
        work_book_sheet.update_cell(row_number, 2, status.string)
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
        # logging.info(f"Delivery Date: {date.string.replace("\n", "").replace("\t", "").strip()}")
        # logging.info(f"Tracking Number: {cell}")

    except Exception as e:
        # Log any exceptions that occur during the execution
        logging.error(f"An error occurred for row {row_number}: {e}")
