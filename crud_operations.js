#to create a new database
use userdb;

#to create a new collection
db.createCollection("users")

#create_operation to insert a single document into a collection
db.users.insertOne({name: "Angela", age: 27,});

#create_operation to insert multiple documents into a collection
db.users.insertMany([
    {
        name: "Angela",
        age: 27,
    },
    {
        name: "Dwight",
        age: 30,
        
    },
    {
        name: "Jim",
        age: 29,
    }
]);

#read_operations
#to retrieve data from a collection we use find() method
db.users.find()

#to retrieve a single document object
db.users.findOne({ name: "Jim" })

#update_operations
#to update single document
db.users.updateOne({ name: "Angela" }, { $set: { email: "angela@gmail.com" } })

#to update multiple documents
db.users.updateMany({ age: { $lt: 30 } }, { $set: { status: "active" } })

#delete_operations
#to remove a single document
db.users.deleteOne({ name: "Angela" })

#to remove multiple documnets
db.users.deleteMany({ age: { $lt: 30 } })

#to remove an entire collection
db.users.drop()
