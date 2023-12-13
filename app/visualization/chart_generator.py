from flask import Blueprint, render_template, jsonify, request, current_app
from datetime import datetime, timedelta
import json
from bson import json_util

visualization_app = Blueprint('visualization_app', __name__)

def parse_json(data):
    return json.loads(json_util.dumps(data))

# Route to display the dashboard
@visualization_app.route('/')
def display_dashboard():
    return render_template('dashboard.html')


# API endpoint to get information about a particular record by ID column in dataset
@visualization_app.route('/api/items/<item_id>', methods=['GET'])
def get_item_by_id(item_id):
    item = current_app.config['collection'].find_one({'id': item_id})
    return parse_json(item)

#API endpoint to get information about a records from given ranges
@visualization_app.route('/api/items/range', methods=['GET'])
def get_items_within_range():
    try:
        # Get the start and end dates from the request parameters
        start_date_str = request.args.get('start_date')
        end_date_str = request.args.get('end_date')

        # Define the query to filter items within the specified date range
        query = {
            "updated_on": {"$gte": start_date_str, "$lt": end_date_str}
        }

        # Fetch items within the specified date range
        items = list(current_app.config['collection'].find(query))

        return parse_json(items)

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# API endpoint to get information about top 10 crimes in Chicago
@visualization_app.route('/api/top_10_crimes', methods=['GET'])
def top_10_crimes():
    pipeline = [
        {"$group": {"_id": "$primary_type", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    data = list(current_app.config['collection'].aggregate(pipeline))
    return jsonify(data)

# API endpoint to get information about arrests
@visualization_app.route('/api/arrests', methods=['GET'])
def arrests_info():
    pipeline = [
        {"$group": {"_id": "$arrest", "count": {"$sum": 1}}}
    ]
    data = list(current_app.config['collection'].aggregate(pipeline))
    return jsonify(data)

# API endpoint to get the top 5 most crimes occurred locations
@visualization_app.route('/api/top_5_most_occurred_locations', methods=['GET'])
def top_5_most_occurred_locations():
    pipeline = [
        {"$group": {"_id": "$location_description", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 5}
    ]

    data = list(current_app.config['collection'].aggregate(pipeline))
    return jsonify(data)

