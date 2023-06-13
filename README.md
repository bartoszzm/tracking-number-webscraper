<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<h3 align="center">ptracking-number-webscraper
</h3>

  <p align="center">
    <br />
    <a href="https://github.com/bartoszzm/tracking-number-webscraper"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/bartoszzm/tracking-number-webscraper">View Demo</a>
    ·
    <a href="https://github.com/bartoszzm/tracking-number-webscraper/issues">Report Bug</a>
    ·
    <a href="https://github.com/bartoszzm/tracking-number-webscraper/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This Python project utilizes various libraries and APIs to automate tracking shipments using USPS tracking numbers. It connects to a Google Sheet, retrieves tracking numbers, and sends HTTP requests to the USPS website. It parses the HTML response to extract delivery status and date information, which is then updated back into the Google Sheet. The script also includes error handling and logging for verification purposes. Overall, it streamlines the process of tracking shipments and keeping the Google Sheet up-to-date with the latest information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Python 3.11
* Beautifulsoup4 
* Google Sheet API
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

1. In order to have this project started you will need to install pip.
   With pip installed you will require these packages to be installed:
    ```sh
    pip install beautifulsoup4
    pip install requests
    pip install gspread
    ```
2. In order to get the script running you have to enable Google Sheet API for your Google Sheet.
   Follow the link below to learn how to do it:
   * https://support.google.com/googleapi/answer/6158841?hl=en
   * https://support.google.com/googleapi/answer/6158862?hl=en&ref_topic=7013279&sjid=7464328562354771065-EU

3. Download your service_account.json and place it into the scrpit folder location.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

This project is a Python script that utilizes various libraries and APIs to track shipments using USPS tracking numbers.
2. Importing necessary libraries: The script imports the `time`, `logging`, `BeautifulSoup` from `bs4`, `requests`, and `gspread` libraries.
3. Setting up logging: The logging module is configured to log messages with the timestamp, severity level, and message content.
4. Connecting to the Google Sheet: The script establishes a connection to a Google Sheet named "Get tracking" using the `gspread` library and assigns the worksheet named "testing" to the `work_book_sheet` variable.
5. Setting the user-agent header: The script sets the user-agent header in the HTTP requests to mimic a browser.
6. Getting the total number of rows: The script retrieves the total number of rows in the worksheet using the `row_count` property of the `work_book_sheet` object.
7. Iterating over the rows: The script uses a `for` loop to iterate over the rows in the worksheet, from 1 to the total number of rows.
8. Tracking number retrieval: For each row, the script retrieves the tracking number from the first cell of that row in the Google Sheet.
9. Checking for an empty cell: The script checks if the retrieved tracking number cell is empty. If it is empty, the loop is stopped, and a message is logged.
10. Constructing the tracking URL: The script constructs a URL for USPS tracking by appending the tracking number to the base URL.
11. Sending a GET request: The script sends a GET request to the USPS website using the constructed tracking URL and the specified headers.
12. Parsing the HTML response: The script uses BeautifulSoup to parse the HTML content of the USPS website response.
13. Extracting delivery status and date: The script extracts the delivery status and date information from the parsed HTML.
14. Updating the Google Sheet: The script updates the Google Sheet by writing the delivery status and date information into the respective cells of the current row.
15. Logging and verification: The script logs the tracking URL and delivery status for verification purposes.
16. Delaying between iterations: The script introduces a 2-second delay before processing the next row to avoid overwhelming the USPS website.
17. Error handling: The script includes exception handling to log any errors that occur during the execution, specifying the row number and the corresponding error message.
18. Additional checking (optional): There are commented-out lines that can be uncommented to print the delivery date and tracking number from the cell for further verification.

Overall, this script automates the process of retrieving tracking numbers from a Google Sheet, querying the USPS website for delivery status, and updating the Google Sheet with the obtained information.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/Bartosszzmm) - musiolbartosz@gmail.com  

Project Link: [[https://github.com/github_username/repo_name](https://github.com/bartoszzm/tracking-number-webscraper/tree/main)]([https://github.com/github_username/repo_name](https://github.com/bartoszzm/tracking-number-webscraper/tree/main))

<p align="right">(<a href="#readme-top">back to top</a>)</p>
