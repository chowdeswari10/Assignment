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
    new_product ={
               "productName":"sofa",
			   "price":599,
			   "type":"cash",
			   "method":"store",
			   "quantity":10}

    # Write an expression that inserts the 'new_product' document into the 'products' collection.
    result = accounts_collection.insert_one(new_product)

    document_id = result.inserted_id
    pprint(f"_id of inserted document: {document_id}")


except Exception as e:
    print(e)
finally:
    client.close()