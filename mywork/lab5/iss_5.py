#!/usr/bin/env python

import logging
import pandas as pd
import requests
import os
import mysql.connector


DBHOST = os.environ.get('DBHOST')
DBUSER = os.environ.get('DBUSER')
DBPASS = os.environ.get('DBPASS')
DB = "iss"

def register_reporter(table = 'reporters', reporter_id = 'xak2wm', reporter_name = 'Nina Breen'):
    try:
        db = mysql.connector.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DB)
        cursor = db.cursor(dictionary=True)
        query = f"SELECT reporter_id FROM {table} WHERE reporter_id = %s"
        cursor.execute(query, (reporter_id,))
        results = cursor.fetchone()

        if results:
            logging.info("Reporter already exists.")
        else:
            ins_query = f"INSERT INTO {table} (reporter_id, reporter_name) VALUES (%s,%s)"
            ins_report = (reporter_id, reporter_name)
            cursor.execute(ins_query, ins_report)
            db.commit()
            logging.info("Reporter registered.")
    except mysql.connector.Error as e:
        logging.error(f"Error has occurred during regestration, {e}.")
    finally:
        cursor.close()
        db.close()


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
    trans_data['timestamp'] = pd.to_datetime(trans_data['timestamp'], unit='s')
    logging.info("Data transformed successfully.")
    return trans_data

def load(data, reporter_id = 'xak2wm'):
    try:   
        db = mysql.connector.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DB)
        cursor = db.cursor()
        message = data.loc[0,'message']
        latitude = float(data.loc[0, 'iss_position.latitude'])
        longitude = float(data.loc[0, 'iss_position.longitude'])
        timestamp = data.loc[0, 'timestamp'].strftime('%Y-%m-%d %H:%M:%S')

        query = "INSERT INTO locations (message, latitude, longitude, timestamp, reporter_id) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (message, latitude, longitude, timestamp, reporter_id))
        db.commit()
        logging.info("Data inserted into database.")
    except mysql.connector.Error as e:
        logging.error(f"Error has occurred in load step, {e}.")
    finally:
        cursor.close()
        db.close()



def main():
    register_reporter()
    raw_data = extract()
    if raw_data:
        transformed_data = transform(raw_data)
        load(transformed_data)
        logging.info("ETL process completed.")

if __name__ == "__main__":
    main()
