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
    accounts_collection = db.products

    # retrieving one product
    doccument_to_find = {
        "_id": ObjectId("65d63ab8e2c12cea02e54da7")
    }

    result = accounts_collection.find_one(doccument_to_find)

    pprint.pprint(result)


except Exception as e:
    print(e)
finally:
    client.close()