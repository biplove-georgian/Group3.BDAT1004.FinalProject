# Import All Required Libraries
from flask import Flask
from api.data_transformer import data_transformer_app
from visualization.chart_generator import visualization_app
from database.mongodb_connector import get_mongo_collection
from config import Config

app = Flask(__name__)
app.config.from_object(Config)  # Load configurations from the Config class

# Set the collection attribute on the app config
app.config['collection'] = get_mongo_collection(app.config['MONGODB_URI'])

app.register_blueprint(data_transformer_app)
app.register_blueprint(visualization_app)

if __name__ == '__main__':
    app.run(debug=True)
