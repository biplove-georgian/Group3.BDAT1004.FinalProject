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


def parse_json(data):
    return json_util.loads(json_util.dumps(data))

@visualization_app.route('/api/items/range', methods=['GET'])
def get_range_of_items():
    # Get the end date (defaults to the current date)
    end_date_str = request.args.get('end_date', str(datetime.utcnow().date()))
    end_date = parse_date(end_date_str)

    # Calculate the start date (defaults to 24 hours before the end date)
    start_date_str = request.args.get('start_date', str(end_date - timedelta(days=1)))
    start_date = parse_date(start_date_str)

    # Convert date objects to datetime objects
    start_date = datetime.combine(start_date, datetime.min.time())
    end_date = datetime.combine(end_date, datetime.min.time()) + timedelta(days=1)

    # Fetch items within the specified date range
    items = list(current_app.config['collection'].find({
        "updated_on": {"$gte": start_date, "$lt": end_date}
    }))

    return jsonify(parse_json(items))

def parse_date(date_str):
    try:
        # Try parsing date with flexible format
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f").replace(microsecond=0).date()
    except ValueError:
        try:
            # Try parsing date without time information
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError as e:
            # Handle parsing errors
            raise ValueError(f"Error parsing date: {date_str}. {e}")






# API endpoint to get information about a particular record by ID column in dataset
@visualization_app.route('/api/items/<item_id>', methods=['GET'])
def get_item_by_id(item_id):
    item = current_app.config['collection'].find_one({'id': item_id})
    return parse_json(item)


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

