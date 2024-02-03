#logical_and_operator
db.listingsAndReviews.find({$and: [{amenities: "Smoking allowed"}, {amenities: "Pets allowed"}]});

#logical_or_operator
db.listingsAndReviews.find({$or: [{amenities: "Smoking allowed"}, {amenities: "Pets allowed"}]});

#logical_nor_operator
db.listingsAndReviews.find({$nor: [{amenities: "Smoking allowed"}, {amenities: "Pets allowed"}]});

#logical_not_operator
#insert_data
db.student.insertMany([
        {
                "f_name" : "Zenny",
                "sex" : "Female",
                "class" : "VI",
                "age" : 12,
                "grd_point" : 32.6342
        },
        {
                "f_name" : "Paul",
                "sex" : "Male",
                "class" : "VII",
                "age" : 13,
                "grd_point" : 29.5904
        },
        {
                "f_name" : "Tom",
                "sex" : "Male",
                "class" : "VI",
                "age" : 11,
                "grd_point" : 30.1257
        },
        {
                "f_name" : "Lassy",
                "sex" : "Female",
                "class" : "VIII",
                "age" : 13,
                "grd_point" : 28.2514
        },
        {
                "f_name" : "Peter",
                "sex" : "Male",
                "class" : "VI",
                "age" : 11,
                "grd_point" : 31.5201
        }
]			
)

db.student.find( {"age": { $not: {$lt : 12}}});

#insertOne
db.grades.insertOne({
  student_id: 654321,
  products: [
    {
      type: "exam",
      score: 90,
    },
    {
      type: "homework",
      score: 59,
    },
    {
      type: "quiz",
      score: 75,
    },
    {
      type: "homework",
      score: 88,
    },
  ],
  class_id: 550,
})

#insertMany
db.grades.insertMany([
  {
    student_id: 546789,
    products: [
      {
        type: "quiz",
        score: 50,
      },
      {
        type: "homework",
        score: 70,
      },
      {
        type: "quiz",
        score: 66,
      },
      {
        type: "exam",
        score: 70,
      },
    ],
    class_id: 551,
  },
  {
    student_id: 777777,
    products: [
      {
        type: "exam",
        score: 83,
      },
      {
        type: "quiz",
        score: 59,
      },
      {
        type: "quiz",
        score: 72,
      },
      {
        type: "quiz",
        score: 67,
      },
    ],
    class_id: 550,
  },
  {
    student_id: 223344,
    products: [
      {
        type: "exam",
        score: 45,
      },
      {
        type: "homework",
        score: 39,
      },
      {
        type: "quiz",
        score: 40,
      },
      {
        type: "homework",
        score: 88,
      },
    ],
    class_id: 551,
  },
])
#comparison_operators
#greaterThan_operator
db.grades.find({ "products.score": { $gt: 50 } })

#greateThanEqualTo_operator
db.grades.find({ "products.score": { $gte: 50 } })

#lesserThan_operator
db.grades.find({ "products.score": { $lt: 70 } })

#lesserThanEqualto_operator
db.grades.find({ "products.score": { $lt: 70 } })

#andoror
db.listingsAndReviews.find({
  $and: [
    {$or: [{amenities: "Oven"}, {amenities: "Iron"}]},
    {$or: [{amenities: "Microwave"}, {amenities: "TV"}]},
  ],
});

#mongoDBPy
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://mchowdeswari007:sowmya21@cluster0.3wm2fac.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    '''for db_name in client.list_database_names():
        print(db_name)*/''' #once sucessfully established connection
except Exception as e:
    print(e)

#output
PS C:\Users\mchow\OneDrive\Pictures> & C:/Users/mchow/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/mchow/Downloads/from pymongo.py"
Pinged your deployment. you successfully connected to MongoDB!

#in
db.grades.find({ student_id: { $in: [654321, 546789] } })

#findArray
db.listingsAndReviews.find({amenities: "TV"});

#elementsMatch
db.listingsAndReviews.find({amenities: {$elemMatch: {$eq: "Kitchen"}}});

