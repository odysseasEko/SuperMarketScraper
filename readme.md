# kavaSpider - Web Scraping Sklavenitis Kava Products

## Introduction
This Python script is designed to scrape product information from the Sklavenitis website's Kava section. It uses the Scrapy framework to crawl through multiple pages and extract data about Kava products, including the product name, price, and link to the product page.

## Prerequisites
Before running this script, make sure you have the following dependencies installed:
- Python (3.6 or higher)
- Scrapy

You can install Scrapy using pip:
```bash
pip install scrapy
```

## Usage
1. Clone or download this repository to your local machine.

2. Navigate to the project directory in your terminal:
```bash
cd path/to/kavaSpider
```

3. To start the web scraping process, run the following command:
```bash
scrapy crawl kavaExt
```

4. The script will begin crawling the Sklavenitis Kava pages and extracting product information. The data will be saved to the standard output (usually the terminal).

## Configuration
You can customize the script's behavior by modifying the `kavaSpider` class in the `kava_spider.py` file.

- `name`: The name of the Spider, which you can change to something more descriptive if needed.

- `start_urls`: A list of URLs to start crawling. You can add or remove URLs as needed to target different sections of the website.

- `parse`: This method defines how the data is extracted from the web pages. You can adjust the CSS selectors to match the website's structure if it changes.

## Output
The script will output the scraped data in JSON format with the following fields for each product:
- `name`: The name of the Kava product.
- `price`: The price of the Kava product.
- `link`: The URL link to the product's page on the Sklavenitis website.

## Disclaimer
Please be mindful of the website's terms of use and scraping policies. Web scraping may be subject to legal restrictions or terms of service of the website. Make sure your web scraping activities comply with these rules.

## License
This script is provided under the MIT License. Feel free to modify and use it according to your needs.