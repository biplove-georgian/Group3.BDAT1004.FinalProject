# Chicago Crime Dashboard

## Overview

This Flask web application serves as a Chicago Crime Dashboard, providing visualizations and insights based on crime data from the City of Chicago. The application fetches data from the Chicago Crime API, stores it in a MongoDB database, and visualizes it using Google Charts.

## Project Hierarchy

```plaintext
GROUP3.BDAT1004.FINALPROJECT/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── data_transformer.py
│   ├── visualization/
│   │   ├── __init__.py
│   │   ├── chart_generator.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── mongodb_connector.py
│   ├── templates/
│       ├── dashboard.html
│   ├── app_config.py
├── scripts/
│   ├── import_data_script.py
    ├── script_config.py
├── requirements.txt
├── README.md
├── .gitignore
```

## Project Structure

- **`app/`**: Contains the main application logic.
  - **`main.py`**: Entry point for the Flask application.
  - **`api/`**: Module for handling API-related functionality.
    - **`data_transformer.py`**: Blueprint for retrieving required data.
  - **`visualization/`**: Module for handling data visualization.
    - **`chart_generator.py`**: Blueprint for generating charts and displaying the dashboard.
  - **`database/`**: Module for database-related functionality.
    - **`mongodb_connector.py`**: Helper functions for connecting to MongoDB.
  - **`templates/`**: Contains HTML templates, including `dashboard.html`.

- **`scripts/`**: Contains scripts related to the project.
  - **`data_import_script.py`**: Script for importing data from the Chicago Crime API every 24 hours.

- **`config.py`**: Configuration file for Flask application settings.

- **`requirements.txt`**: List of Python dependencies for the project.

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/biplove-georgian/Group3.BDAT1004.FinalProject.git
   cd Group3.BDAT1004.FinalProject
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up MongoDB:**

   - Create a MongoDB Atlas account or use a local MongoDB instance.
   - Update the MongoDB URI in `config.py`.

4. **Run the Application:**

   ```bash
   python3 app/main.py
   ```

   Visit [http://localhost:5000](http://localhost:5000) in your browser.

## Running Data Import Script

To run the data import script, execute the following command:

```bash
python scripts/data_import_script.py
```

This script fetches data from the Chicago Crime API and stores it in the MongoDB database.

## Configuration

- **`config.py`**: Update the MongoDB URI and other configuration settings.

## Contributing

Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Feel free to customize this README further according to your project's needs.