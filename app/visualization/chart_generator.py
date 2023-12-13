# app/visualization/chart_generator.py
from flask import Blueprint, render_template, jsonify, request, current_app
import json
from bson import json_util

visualization_app = Blueprint('visualization_app', __name__)


def parse_json(data):
    return json.loads(json_util.dumps(data))


# Route to display the dashboard
@visualization_app.route('/')
def display_dashboard():
    return render_template('dashboard.html')

# API endpoint to retrieve data
@visualization_app.route('/api/items/range', methods=['GET'])
def get_range_of_items():
    start_date = request.args.get('date')  
    end_date = request.args.get('date')

    # Example: Fetch items within a date range
    items = list(current_app.config['collection'].find({
        "date_field": {"$gte": start_date, "$lte": end_date}
    }))

    return jsonify(items)

@visualization_app.route('/api/items/<item_id>', methods=['GET'])
def get_item_by_id(item_id):
    item = current_app.config['collection'].find_one({'_id': item_id})
    return jsonify(item)

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

# API endpoint to get the top 5 most occurred locations
@visualization_app.route('/api/top_5_most_occurred_locations', methods=['GET'])
def top_5_most_occurred_locations():
    pipeline = [
        {"$group": {"_id": "$location_description", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 5}
    ]

    data = list(current_app.config['collection'].aggregate(pipeline))
    return jsonify(data)

