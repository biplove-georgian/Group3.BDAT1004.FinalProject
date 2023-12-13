from pymongo import MongoClient

def get_mongo_collection(mongo_uri):
    client = MongoClient(mongo_uri)
    database = client["chicago_crime_db"]
    collection = database['chicago_crime_collection']
    return collection
