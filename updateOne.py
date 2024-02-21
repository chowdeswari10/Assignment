from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint
uri = "mongodb+srv://mchowdeswari007:sowmya21@cluster0.3wm2fac.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'shopping' database
    db = client.shopping

    # Get reference to 'products' collection
    products_collection = db.products

    # Filter
    document_to_update = {"_id": ObjectId("65d63ab8e2c12cea02e54daa")}

    # Update
    add_to_balance = {"$inc": {"price": 50}}

    # Print original document
    pprint.pprint(products_collection.find_one(document_to_update))

    # Write an expression that adds to the target account balance by the specified amount.
    result = products_collection.update_one(document_to_update, add_to_balance)
    print("Documents updated: " + str(result.modified_count))

    # Print updated document
    pprint.pprint(products_collection.find_one(document_to_update))


except Exception as e:
    print(e)
finally:
    client.close()