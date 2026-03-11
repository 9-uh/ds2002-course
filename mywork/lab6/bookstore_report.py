#!/usr/bin/env python3

import os
from pymongo import MongoClient

url = os.getenv("MONGODB_ATLAS_URL")
user = os.getenv("MONGODB_ATLAS_USER")
pwd = os.getenv("MONGODB_ATLAS_PWD")

def main():
    client = MongoClient(url, username = user, password = pwd, connectTimeoutMS=200, retryWrites=True)
    db = client.bookstore
    authors = db.authors

    total = authors.count_documents({})
    print("The total number of authors is " + str(total))
    
    all_info = authors.find({})
    for author in all_info:
        name = author['name']
        nation = author['nationality']
        print(name + " -- " + nation)
    client.close()

if __name__ == "__main__":
    main()
