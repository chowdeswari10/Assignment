db.grades.createIndex({class_id: "hashed"});

#to retrieve the document corresponding to the specified class id
  
db.grades.find({class_id: 551});
