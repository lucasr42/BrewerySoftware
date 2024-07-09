"""
This contains helpers that will create the tables and input/manipulate items in those tables

- This should be a class so I can create a helper object when I run the flask app and 
    call its methods
"""
import boto3
from botocore.exceptions import ClientError


"""
Creates and connects to Inventory and Employee DynamoDB Tables
"""
class Table:
    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb", region_name="us-west-2")

    """
    Initially creates the Inventory table

    *Come back for the GSI.
        - May want to add one on Producer so you can search strictly on Producer
    """
    def create_inventory_table(self):
        inventory_table = self.dynamodb.create_table(
            AttributeDefinitions = [
                {
                    "AttributeName": "product",
                    "AttributeType": "S"
                },
                {
                    "AttributeName": "name",
                    "AttributeType": "S"
                }
            ],
            TableName = "inventory",
            KeySchema = [
                {
                    "AttributeName": "product",
                    "KeyType": "HASH"
                },
                {
                    "AttributeName": "name",
                    "AttributeType": "RANGE"
                }
            ],
            BillingMode = "PROVISIONED",
            ProvisionedThroughput = {
                "ReadCapacityUnits": 5,
                "WriteCapacityUnits": 5,
            },
        )
        print("Creating Inventory Table...")
        inventory_table.wait_until_exists()
        print("Inventory Table created")
        return inventory_table

    """
    Initially creates the Employee table
    """

    """
    Connects to the DDB Inventory Table if it exists
    Creates it if it does not
    """
    def connect_inventory_ddb_table(self):
        try:
            inventory_table = self.dynamodb.Table("inventory")
        except ClientError as e:
            if e.response["Error"]["Code"] == "ResourceNotFoundException":
                print("Inventory Table not Found. Creating...")
                inventory_table = self.create_inventory_table()

        return inventory_table
    

"""
Helpers for CRUD operations on Inventory tables
"""
class Inventory:
    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb", region_name="us-west-2")

    """
    Need methods to create, read, update, and delete inventory
    Malt:
        - add_malt(all attributes)
        - get_malt(name)
        - get_malt(producer)
        - list_malt()
        - update_malt(all attributes)
        - delete_malt(name)

    Hops:
        - add_hops(all attributes)
        - get_hops(name)
        - get_hops(producer)
        - list_hops()
        - update_malt(all attributes)
        - delete_malt(name)

    Yeast:
        - add_yeast(all attributes)
        - get_yeast(name)
        - get_yeast(producer)
        - list_yeast()
        - update_yeast(all attributes)
        - delete_yeast(name)

    Batch:
        - add_batch(all attributes)
        - get_batch(name, batch_number)
        - get_batch(batch_number)
        - list_batch(name)
        - list_batch(date)
        - list_batch(style)
        - update_batch(all attributes)
        - delete_batch(batch_number)

    Keg:
        - add_kegs(all attributes)
        - get_kegs(size)
        - get_kegs(clean)
        - get_kegs(size, clean)
        - update_kegs(all attributes)
        - delete_kegs(size)
    """