import time
from datetime import datetime, timedelta
from pymongo import MongoClient
from script_config import Config
import requests

client = MongoClient(Config.MONGODB_URI)
database = client["chicago_crime_db"]
collection = database['chicago_crime_collection']

def acquire_and_store_data():
    cc_api = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"

    try:
        # Make the request to get all data from the API
        response = requests.get(cc_api)
        response.raise_for_status()

        if response.status_code == 200:
            all_data = response.json()

            # Calculating the timestamp for the start of the current day
            start_date = datetime.utcnow() - timedelta(hours=24)

            # Extracting the date part from the timestamp and convert to ISO format
            start_date_iso = start_date.date().isoformat()

            # Filter data that has been updated in the last 24 hours
            filtered_data = [
                entry for entry in all_data
                if "updated_on" in entry
                and datetime.strptime(entry["updated_on"], "%Y-%m-%dT%H:%M:%S.%f").date().isoformat() >= start_date_iso
            ]

            # Insert filtered data into MongoDB
            collection.insert_many(filtered_data)
            print("Data acquired and stored successfully.")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")

# Run the acquisition process every 24 hours
while True:
    acquire_and_store_data()
    # Wait for 24 hours before fetching data again
    time.sleep(60 * 60 * 24)




