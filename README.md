# ackodrive-cars-portal
# Car Data Scraper

A Python-based web scraping tool to extract car details such as names, prices, features, and image URLs from a given URL. The extracted data is saved in a CSV file for further analysis or use.

## Features

- **HTML Parsing:** Fetch and parse the HTML content from a user-provided URL.
- **Data Extraction:** Extract car names, prices, features, and image URLs using BeautifulSoup.
- **Data Storage:** Save the extracted data into a CSV file.
- **Analytics:** Display counts of anchor tags and image URLs on the web page.
- **Error Handling:** Handles various errors like invalid URLs or issues in saving files.

## Requirements

- Python 3.6 or later
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/car-data-scraper.git
   cd car-data-scraper
