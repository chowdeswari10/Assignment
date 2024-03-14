db.listingAndReviews.createIndex({name: "text"});

db.listingAndReviews.find({ $text: { $search: "Ribeira Charming Duplex"} });
