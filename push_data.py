
import os
import sys
import json


from dotenv import load_dotenv
load_dotenv()


MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca=certifi.where()


import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class NetworkDataExtract():
    def __init__(self,):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json_converter(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection_name = collection  # Use a different name to avoid overwriting
        
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
        
         # Access the collection from the database
            self.collection = self.database[self.collection_name]
        
        # Insert data into the collection
            self.collection.insert_many(records)
            return len(records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
if __name__ == '__main__':
    FILE_PATH = 'Network_Data\phisingData.csv'
    DATABASE="MAYANKAI"
    Collection="NetworkData"
    network_obj=NetworkDataExtract()
    records = network_obj.csv_to_json_converter(file_path=FILE_PATH)
    print(records)
    no_of_records=network_obj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)