```markdown
# Sephora Scraping

A project for scraping product information from Sephora's website using Python and Jupyter Notebook.

## Features

- Extract product prices.
- Extract product features.
- Save data to CSV files.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/ghazalsf/sephora_scrapping.git
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   cd sephora_scrapping
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Usage

1. Run the `get-product-price.py` script to scrape product prices:
   ```sh
   python get-product-price.py
   ```
2. Check the generated CSV files (`product-feature-priced.csv` and `product-features.csv`) for the data.

## Requirements

- Python 3.7 or higher
