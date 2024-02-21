from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint
uri =  "mongodb+srv://mchowdeswari007:sowmya21@cluster0.3wm2fac.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'shopping' database
    db = client.shopping

    # Get reference to 'products' collection
    accounts_collection = db.products

    # retrieving morethan one documents
    documents_to_find = {"price": {"$gt": 400}}

    # Write an expression that selects the documents matching the query constraint in the 'products' collection.
    cursor = accounts_collection.find(documents_to_find)

    num_docs = 0
    for document in cursor:
        num_docs += 1
        pprint.pprint(document)
        print()
    print("# of documents found: " + str(num_docs))


except Exception as e:
    print(e)
finally:
    client.close()