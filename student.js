#creating a database and collection
#student database 
db.createCollection("details")
#inserting data 
#Query 1
db.details.insertOne({Emp_ID: "10025AE336",
Personal_details:{
    First_Name: "Radhika",
    Last_Name: "Sharma",
    Date_Of_Birth: "1995-09-26"
},
Contact: {
    email: "radhika_sharma.123@gmail.com",
    phone: "9848022338"
},
Address: {
    city: "Hyderabad",
    Area: "Madapur",
    State: "Telangana"
}})
#Query 2
db.details.insertOne({id: POST_ID,
title: TITLE_OF_POST,
description: POST_DESCRIPTION,
by: POST_BY,
url: URL_OF_POST,
tags: [TAG1, TAG2, TAG3],
likes: TOTAL_LIKES,
comments: [
     {
     user:'COMMENT_BY',
     message: TEXT,
     dateCreated: DATE_TIME,
     like: LIKES
    },
    { 
     user:'COMMENT_BY',
     message: TEXT,
     dateCreated: DATE_TIME,
     like:LIKES
    }
]
})
