db.student.createIndex({"age":-1},
{
"createdCollectionAutomatically" : false,
"numIndexesBefore" : 1,
"numIndexesAfter" : 2,
"ok" : 1
} )

#to list all the indexes

db.student.getIndexes()
