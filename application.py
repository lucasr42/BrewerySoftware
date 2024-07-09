"""
Driver for the Brewery Software program

- This should contain the backend logic
- It should have routes and methods for receiving calls from the front end
    - Those methods pass data to helpers that input items into the DDB tables
"""

import boto3
from flask import Flask, jsonify, render_template, request
from helpers import Table

application = Flask(__name__)

dynamodb = boto3.resource("dynamodb", region_name="us-west-2")


"""
Connects to Inventory Table
"""
def connect_inventory_table():
    tables = Table()
    inventory_table = tables.connect_inventory_ddb_table()

    return inventory_table

"""
Loads the index page
"""
@application.route('/')
def index():
    print("Request for index page received")
    return render_template("index.html")

# run the app
if __name__ == "__main__":
    application.run()