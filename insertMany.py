#MongoDB crud operations with python
#insertOneUsingCRUD

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
from pprint import pprint

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

    # inserting one product
    new_products =[{
               "productName":"table",
			   "price":800,
			   "type":"card",
			   "method":"store",
			   "quantity":15},
			   
			   {
               "productName":"laptop",
			   "price":655,
			   "type":"cash",
			   "method":"online",
			   "quantity":1},
			   
			   {"productName":"TV",
			   "price":400,
			   "type":"cash",
			   "method":"store",
			   "quantity":10},
			   
			   {"productName":"DVD",
			   "price":16,
			   "type":"card",
			   "method":"online",
			   "quantity":10}]

    # Write an expression that inserts the 'new_products' document into the 'products' collection.
    result = accounts_collection.insert_many(new_products)

    document_ids = result.inserted_ids
    print("# of documents inserted: " + str(len(document_ids)))
    print(f"_ids of inserted documents: {document_ids}")

except Exception as e:
    print(e)
finally:
    client.close()