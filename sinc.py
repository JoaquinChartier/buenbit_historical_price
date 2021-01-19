import urllib3
import json
import os.path as path
import csv
from datetime import datetime
from config_file import * 

def write_headers():
    csv_header = ['daiars_price', 
                    'daiars_purchase', 
                    'daiars_selling', 
                    'daiusd_price', 
                    'daiusd_purchase', 
                    'daiusd_selling', 
                    'btcars_price', 
                    'btcars_purchase', 
                    'btcars_selling', 
                    'datetime']

    #If file not exist, write headers
    if not path.exists(out_file_name):
        with open(out_file_name, mode='w+',encoding="utf-8", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(csv_header)

def write_data(res):
    #Write the new data rows
    actual = datetime.now()
    now = actual.strftime("%Y-%m-%d %H:%M:%S")
    with open(out_file_name, mode='a',encoding="utf-8", newline='\n') as f:
            writer = csv.writer(f)

            data_row = (res["object"]["daiars"]["selling_price"],
                        res["object"]["daiars"]["purchase_price"],
                        res["object"]["daiars"]["selling_price"],
                        res["object"]["daiusd"]["selling_price"],
                        res["object"]["daiusd"]["purchase_price"],
                        res["object"]["daiusd"]["selling_price"],
                        res["object"]["btcars"]["selling_price"],
                        res["object"]["btcars"]["purchase_price"],
                        res["object"]["btcars"]["selling_price"],
                        now)

            writer.writerow(data_row)

def request():
    #Make HTTP request, return a object with the data
    url = "https://be.buenbit.com/api/market/tickers/"
    http = urllib3.PoolManager()
    result = http.request("GET", url)

    print("Making request")
    res = (json.loads(result.data))
    print("Request successfull")
    return res

if __name__ == '__main__':
    res = request()
    write_headers()
    write_data(res)