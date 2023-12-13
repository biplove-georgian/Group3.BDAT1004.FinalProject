# Import Required Libraries
from flask import Blueprint, jsonify, current_app
from bson import json_util

data_transformer_app = Blueprint('data_transformer_app', __name__)

def parse_json(data):
    return json_util.loads(json_util.dumps(data))

@data_transformer_app.route('/api/items', methods=['GET'])
def get_all_items():
    # Project only the specific fields
    projection = {
        "id": 1,
        "case_number": 1,
        "date": 1,
        "block": 1,
        "iucr": 1,
        "primary_type": 1,
        "description": 1,
        "location_description": 1,
        "arrest": 1,
        "domestic": 1,
        "beat": 1,
        "district": 1,
        "ward": 1,
        "community_area": 1,
        "fbi_code":1,
        "year": 1,
        "updated_on": 1,
        "_id": 0  # Exclude the default _id field
    }

    items = list(current_app.config['collection'].find({}, projection))
    return jsonify(parse_json(items))
