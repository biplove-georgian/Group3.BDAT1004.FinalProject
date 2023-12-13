import requests
import time
from app.database.mongodb_connector import collection

def acquire_and_store_data():
    cc_api = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"
    response = requests.get(cc_api)

    if response.status_code == 200:
        data = response.json()
        collection.insert_many(data)
        print("Data acquired and stored successfully.")
    else:
        print(f"Error: {response.status_code}")

# Run the acquisition process every 24 hours
while True:
    acquire_and_store_data()
    # Wait for 24 hours
    time.sleep(60*60*24)
