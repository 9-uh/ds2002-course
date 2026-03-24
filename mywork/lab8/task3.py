#!/usr/bin/env python3
import boto3
import logging
import sys
import os


logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()

def parse_args():
    """
    Parse the command line arguments.
    Returns the input folder and bucket/destination
    """
    input_folder  = sys.argv[1]
    destination = sys.argv[2]
    return input_folder, destination

def upload(input_folder, destination):
    """
    uploading the input_folder to the destination.
    """
    s3 = boto3.client('s3', region_name='us-east-1')
    if '/' in destination:
        bucket, prefix = destination.split('/', 1)
        if not prefix.endswith('/'):
            prefix += '/'
    else:
        bucket = destination
        prefix = ''

    try:
        for filename in os.listdir(input_folder):
            if filename.endswith('.csv') and filename.startswith('results'):
                local_path = os.path.join(input_folder, filename)
                key = prefix + filename
                logging.info(f"Uploading {local_path} to s3://{bucket}/{key}")
                
                with open(local_path, 'rb') as file:
                    s3.put_object(
                        Bucket = bucket,
                        Key = key,
                        Body = file
                    )
                    logging.info(f"Uploaded {filename}.")
    except Exception as e:
        logging.error(f'Error uploading files: {e}')

def main():
    """
    Calling the functions to upload all files.
    """
    input_folder, destination = parse_args()
    upload(input_folder, destination)
    logging.info("All files uploaded.")

if __name__ == "__main__":
    main()

        


