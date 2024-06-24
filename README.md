# REST API for Listing Prizes by Catalog - Documentation

## Introduction

This project provides a REST API to list prizes based on a catalog identifier.

## Setup the Application

#### Prerequisites
- Python 3.7+
#### Installation

1. Clone the repository:
```bash
git clone <repository_url>
cd <repository_directory>
```
2. Create and activate a virtual environment:
```bash
python -m venv .venv
# Linux/MacOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate
```
3. Install the dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application
1. Navigate to the project directory.
2. Start the Flask application:
```bash
python app.py
```

## Database

The project does not implement a database yet, all the dataset is contained in the file `mock_database.py`. If you want to customize the `data`, you can modify the 
data variable.

## Api Class

The API class is the core of the project, it is initialized in the init file and passed in a Flask module instance, this way it registers routes and exceptions in its constructor.

## Testing

1. Ensure the virtual environment is running
2. Run the tests using pytest:
```bash
pytest
```

### Testing with pytest
The tests/test_api.py file contains unit tests for the API using pytest. The tests cover different scenarios to ensure the API works correctly and handles errors gracefully.