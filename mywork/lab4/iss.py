#!/usr/bin/env python

import logging
import pandas as pd
import requests
import sys
import os

output_file  = sys.argv[1]

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[console_handler])

def extract():
    url = "http://api.open-notify.org/iss-now.json"
    logging.info(f"Getting data from {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logging.info("Data extracted successfully.")
        return data
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error occurred: {e}")
        return None
    except requests.exceptions.RequestException as e:
        logging.error(f"Error during data extraction: {e}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None    
    
def transform(data):
    logging.info("Cleaning and organizing data.")
    trans_data = pd.json_normalize(data)
    trans_data = trans_data.drop(columns=['message'])
    trans_data['timestamp'] = pd.to_datetime(trans_data['timestamp'], unit='s')
    logging.info("Data transformed successfully.")
    return trans_data

def load(data, output_file):
    logging.info("Loading data to CSV file.")
    if os.path.exists(output_file):
        logging.info(f"Appending data to {output_file}")
        existing_data = pd.read_csv(output_file)
        combined_data = pd.concat([existing_data, data], ignore_index=True)
        combined_data.to_csv(output_file, index=False)
    else:
        logging.info(f"Creating new file {output_file}")
        data.to_csv(output_file, index=False)

def main():
    raw_data = extract()
    if raw_data:
        transformed_data = transform(raw_data)
        load(transformed_data, output_file)
        logging.info("ETL process completed.")

if __name__ == "__main__":
    main()
